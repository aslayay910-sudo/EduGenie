# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant designed to simplify learning using Generative AI. It helps learners ask questions, understand complex topics, generate quizzes, summarize long texts, and get structured learning paths.

---

## 🚀 Features

- **Q&A Module:** Get precise answers for academic and general queries using Google Gemini 1.5 Pro.
- **Concept Explanation:** Simplified explanations for complex topics powered by the lightweight `LaMini-Flan-T5-783M` model.
- **Quiz Generator:** Generate JSON-formatted multiple-choice questions (MCQs) with automated options and answers.
- **Text Summarizer:** Summarize lengthy educational materials into concise key points.
- **Learning Path Generator:** Receive structured, step-by-step learning roadmaps with recommended resources.

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python 3.10+
- **Frontend:** HTML5, CSS3, Jinja2 Templates
- **AI Models:** Google Gemini 1.5 Pro (API), LaMini-Flan-T5-783M (Local)
- **Server:** Uvicorn (ASGI)

---

## 📁 Project Structure

```text
EduGenie/
│-- main.py                  # FastAPI application entry point
│-- explanation_module.py    # Concept explanation logic
│-- qna.py                   # Question answering logic
│-- quiz_module.py           # Quiz generation logic
│-- summary_module.py        # Text summarization logic
│-- learning_path.py         # Personalized roadmap recommendations
│-- templates/
│   └── index.html           # HTML frontend template
│-- static/
│   └── style.css            # Custom CSS styles
└── requirements.txt         # Project dependencies
