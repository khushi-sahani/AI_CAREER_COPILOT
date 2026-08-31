# 🤖 AI Career Copilot

AI Career Copilot is an AI-powered career assistance web application that helps users analyze their resumes, identify relevant skills, and get personalized career guidance based on their career goals.

## ✨ Features

* 📄 Resume analysis
* 🎯 Goal-based career evaluation
* 🧠 AI-powered recommendations
* 🔍 Relevant skill extraction
* 📊 Career/skill gap insights
* 💬 Personalized career guidance
* 🗄️ Database integration for storing application data

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Python, Flask
* **AI:** OpenAI API / Ollama
* **Database:** TiDB Cloud / MySQL
* **ORM:** SQLAlchemy
* **Deployment:** Render
* **Version Control:** Git & GitHub

## 📁 Project Structure

```text
AI_CAREER_COPILOT/
│
├── app.py
├── ai.py
├── requirements.txt
├── templates/
│   └── ...
├── static/
│   └── ...
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/khushi-sahani/AI_CAREER_COPILOT.git
cd AI_CAREER_COPILOT
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key
DATABASE_URL=your_database_url
```

Never commit your `.env` file or API keys to GitHub.

## ▶️ Run Locally

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## 🚀 Deployment

The application can be deployed as a Flask web service using Render.

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
gunicorn app:app
```

## 🎯 Purpose

AI Career Copilot is designed to make career preparation more personalized by connecting a user's resume, career goals, and relevant skills into one AI-powered platform.

## 🔮 Future Improvements

* Personalized learning roadmaps
* Job recommendation system
* Resume improvement suggestions
* Skill-gap visualization
* Interview preparation
* Job description matching
* Progress tracking

## 👩‍💻 Author

**Khushi Sahani**

B.Tech CSE Student

GitHub: https://github.com/khushi-sahani
