# 🤖 AI Career Copilot

An AI-powered career assistant that analyzes resumes, identifies missing skills, calculates an ATS-style score, generates a personalized learning roadmap, and prepares role-specific interview questions.

## 🚀 Live Demo

**Live Application:**
https://ai-career-copilot-7.onrender.com

## 📌 Features

* 📄 Upload resume in **PDF/DOCX** format
* 📝 Paste resume directly into the application
* 🎯 Enter a target career role
* 🤖 AI-powered resume analysis using **Google Gemini**
* 📊 ATS-style resume score
* 💡 Identify relevant skills
* 📌 Identify missing skills for the target role
* 🗺️ Personalized learning roadmap
* 🎯 Role-specific interview questions
* 👤 User Signup & Login
* 🕒 Resume analysis history
* 🗄️ Database storage for user reports
* 🔐 Environment-variable based API key configuration
* 🌐 Deployed as a live web application

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Backend

* Python
* Flask
* SQLAlchemy

### AI

* Google Gemini API
* Google GenAI SDK

### Database

* MySQL / TiDB

### Deployment

* Render
* Gunicorn

### Other Tools

* Git
* GitHub
* VS Code

## 🏗️ Project Architecture

```text
User
  │
  ▼
Flask Web Application
  │
  ├── Authentication
  │     ├── Signup
  │     ├── Login
  │     └── Logout
  │
  ├── Resume Processing
  │     ├── PDF
  │     └── DOCX
  │
  ├── Gemini AI
  │     ├── Skills Analysis
  │     ├── ATS Score
  │     ├── Missing Skills
  │     ├── Career Roadmap
  │     └── Interview Questions
  │
  └── Database
        └── Analysis History
```

## 📂 Project Structure

```text
AI_CAREER_COPILOT/
│
├── app.py
├── ai.py
├── db.py
├── models.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── history.html
│   ├── login.html
│   └── signup.html
│
└── static/
    └── style.css
```

## ⚙️ How It Works

1. User creates an account.
2. User logs into the application.
3. User uploads or pastes their resume.
4. User enters their target career role.
5. The application extracts the resume content.
6. Gemini analyzes the resume according to the target role.
7. The system generates:

   * ATS score
   * Relevant skills
   * Missing skills
   * Personalized roadmap
   * Interview questions
8. The analysis is stored in the database.
9. Users can view previous analyses through the History section.

## 🔧 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/khushi-sahani/AI_CAREER_COPILOT.git
cd AI_CAREER_COPILOT
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
DATABASE_URL=your_database_url_here
```

**Never commit `.env` or API keys to GitHub.**

### 6. Run the application

```bash
python app.py
```

Open:

text
http://127.0.0.1:5000


## 🔐 Security

Sensitive credentials are stored using environment variables.

The following files should not be committed:

```text
.env
venv/
```

## 🎯 Future Improvements

* 📈 Advanced ATS scoring system
* 📄 Resume improvement suggestions
* 📊 Skill-gap visualization
* 🎤 AI mock interview
* 💼 Job recommendation system
* 📧 Job application tracking
* 👤 User profile and career preferences
* 📱 Improved mobile UI
* ⚡ Faster AI response processing

## 👩‍💻 Author

**Khushi Sahani**

B.Tech Computer Science & Engineering

GitHub:
https://github.com/khushi-sahani

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.


