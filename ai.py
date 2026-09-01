from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)


def analyze_resume(resume_text, user_goal):

    prompt = """
You are an experienced technical recruiter and career advisor.

Analyze this resume for the target career.

TARGET ROLE:
""" + user_goal + """

RESUME:
""" + resume_text + """

STRICT RULES:

1. Extract ONLY skills actually present in the resume.
2. Extract only skills relevant to the target role.
3. Identify important skills required for the target role but missing from the resume.
4. Do NOT invent skills, projects, internships, certifications, or experience.
5. Calculate an ATS score from 0 to 100.
6. Give 3 to 5 practical ATS improvement suggestions.
7. Create a roadmap ONLY for missing skills.
8. For every missing skill provide learning steps and one practical project.
9. Generate 8 to 10 realistic interview questions.
10. Interview questions must include technical, project-based, resume-based,
    scenario-based and target-role questions.
11. Questions should feel like real interviews.
12. Keep recommendations realistic for a college student.
13. Return ONLY valid JSON.
14. Do NOT use markdown.
15. Do NOT use ```json.

RETURN EXACTLY THIS JSON STRUCTURE:

{
    "ats_score": 0,
    "ats_feedback": [],
    "skills": [],
    "missing_skills": [],
    "roadmap": [
        {
            "skill": "",
            "learning_steps": [],
            "practice_project": ""
        }
    ],
    "interview_questions": []
}
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "temperature": 0.3
            }
        )

        result = json.loads(response.text)

        return {
            "ats_score": result.get("ats_score", 0),
            "ats_feedback": result.get("ats_feedback", []),
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
            "ats_score": 0,
            "ats_feedback": [],
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e)
        }