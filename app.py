from flask import Flask, render_template, request, redirect, session
from db import Base, engine, SessionLocal
from ai import analyze_resume

import models
import PyPDF2
import docx
import json


app = Flask(__name__)

# Secret key for session
app.secret_key = "your_secret_key"


# Create database tables
Base.metadata.create_all(bind=engine)


# =========================
# HOME
# =========================
@app.route("/")
def home():

    if "user_id" in session:
        return redirect("/dashboard")

    return redirect("/login")


# =========================
# SIGNUP
# =========================
@app.route("/signup", methods=["GET", "POST"])
def signup():

    db = SessionLocal()

    try:

        if request.method == "POST":

            email = request.form["email"]
            password = request.form["password"]

            # Check if user already exists
            existing_user = (
                db.query(models.User)
                .filter_by(email=email)
                .first()
            )

            if existing_user:
                return "User already exists. Please log in."

            # Create new user
            new_user = models.User(
                email=email,
                password=password
            )

            db.add(new_user)
            db.commit()

            return redirect("/login")

        return render_template("signup.html")

    finally:
        db.close()


# =========================
# LOGIN
# =========================
@app.route("/login", methods=["GET", "POST"])
def login():

    db = SessionLocal()

    try:

        if request.method == "POST":

            email = request.form["email"]
            password = request.form["password"]

            # Find user
            user = (
                db.query(models.User)
                .filter_by(
                    email=email,
                    password=password
                )
                .first()
            )

            if user:

                # Save user information in session
                session["user_id"] = user.id
                session["user_email"] = user.email

                return redirect("/dashboard")

            return "Invalid email or password."

        return render_template("login.html")

    finally:
        db.close()


# =========================
# DASHBOARD
# =========================
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    # User must be logged in
    if "user_id" not in session:
        return redirect("/login")

    result = None

    if request.method == "POST":

        # Get user's career goal
        user_goal = request.form.get("role", "").strip()

        # Get pasted resume
        resume_text = request.form.get("resume", "").strip()

        # Get uploaded file
        file = request.files.get("file")


        # =========================
        # FILE HANDLING
        # =========================

        if file and file.filename:

            # ---------- PDF ----------
            if file.filename.lower().endswith(".pdf"):

                try:

                    pdf_reader = PyPDF2.PdfReader(file)

                    resume_text = ""

                    for page in pdf_reader.pages:

                        text = page.extract_text()

                        if text:
                            resume_text += text

                except Exception as e:

                    result = {
                        "error": f"PDF error: {str(e)}"
                    }


            # ---------- DOCX ----------
            elif file.filename.lower().endswith(".docx"):

                try:

                    document = docx.Document(file)

                    resume_text = ""

                    for paragraph in document.paragraphs:

                        resume_text += paragraph.text + "\n"

                except Exception as e:

                    result = {
                        "error": f"DOCX error: {str(e)}"
                    }


            # ---------- INVALID FILE ----------
            else:

                result = {
                    "error": "Invalid file format. Please upload PDF or DOCX."
                }


        # =========================
        # VALIDATION
        # =========================

        if not resume_text:

            result = {
                "error": "Please paste your resume or upload a PDF/DOCX file."
            }

        elif not user_goal:

            result = {
                "error": "Please enter your career goal."
            }


        # =========================
        # AI ANALYSIS
        # =========================

        if resume_text and user_goal and not result:

            try:

                # Analyze resume using AI
                result = analyze_resume(
                    resume_text,
                    user_goal
                )


                # =========================
                # SAVE REPORT TO DATABASE
                # =========================

                db = SessionLocal()

                try:

                    user = (
                        db.query(models.User)
                        .filter_by(id=session["user_id"])
                        .first()
                    )

                    if user:

                        report = models.Report(
                            user_id=user.id,
                            resume_text=resume_text,
                            result=json.dumps(result)
                        )

                        db.add(report)
                        db.commit()

                finally:

                    db.close()


            except Exception as e:

                result = {
                    "error": f"AI error: {str(e)}"
                }


    # =========================
    # SHOW DASHBOARD
    # =========================

    return render_template(
        "dashboard.html",
        result=result,
        user_email=session.get("user_email")
    )


# =========================
# HISTORY
# =========================
@app.route("/history")
def history():

    # User must be logged in
    if "user_id" not in session:
        return redirect("/login")

    db = SessionLocal()

    try:

        # Get logged-in user
        user = (
            db.query(models.User)
            .filter_by(id=session["user_id"])
            .first()
        )

        if not user:
            return redirect("/login")


        # Get user's reports
        reports = (
            db.query(models.Report)
            .filter_by(user_id=user.id)
            .all()
        )


        parsed_reports = []


        for report in reports:

            try:

                parsed_result = json.loads(report.results)

            except Exception:

                parsed_result = {}


            parsed_reports.append({
                "resume": report.resume_text,
                "result": parsed_result
            })


        return render_template(
            "history.html",
            reports=parsed_reports
        )


    finally:

        db.close()


# =========================
# LOGOUT
# =========================
@app.route("/logout")
def logout():

    # Clear session
    session.clear()

    return redirect("/login")


# =========================
# RUN APPLICATION
# =========================
if __name__ == "__main__":

    app.run(debug=True)

