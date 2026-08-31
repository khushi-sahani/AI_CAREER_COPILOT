from ollama import chat
import json


def analyze_resume(resume_text, user_goal):

    prompt = f"""
Evaluate this resume for the user's target career.

Target role:
{user_goal}

STRICT RULES:
- Extract only skills relevant to the target role.
- Do not include irrelevant skills.
- Identify important missing skills.
- Generate a roadmap only for missing skills.
- Generate useful interview questions for the target role.
- Keep recommendations practical for a student.
- Return ONLY valid JSON.
- Do not write markdown.
- Do not write ```json.

Return exactly this structure:

{{
    "skills": [],
    "missing_skills": [],
    "roadmap": [],
    "interview_questions": []
}}

RESUME:

{resume_text}
"""

    try:

        response = chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an experienced technical recruiter "
                        "and career advisor."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            format="json"
        )

        content = response["message"]["content"]

        result = json.loads(content)

        return {
            "skills": result.get("skills", []),
            "missing_skills": result.get("missing_skills", []),
            "roadmap": result.get("roadmap", []),
            "interview_questions": result.get(
                "interview_questions",
                []
            )
        }

    except Exception as e:

        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }