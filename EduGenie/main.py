import os
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
import google.generativeai as genai
from explanation_module import explain_topic
from qna_module import answer_question_with_gemini
from summary_module import summarize_text
from learning_path import get_learning_recommendations
from quiz_module import generate_quiz

# 1. First create the app instance
app = FastAPI(title="EduGenie")

# 2. Configure API key
API_KEY = os.environ.get("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

# 3. Root route to serve index.html (app create pannadhukku appram ezhudhanum)
@app.get("/")
async def read_index():
    return FileResponse("templates/index.html")

# Q&A POST API
@app.post("/qa")
async def answer_question(request: Request):
    data = await request.json()
    question = data.get("question")
    
    if not question:
        return JSONResponse(content={"error": "Please provide a question."}, status_code=400)
    
    answer = answer_question_with_gemini(question)
    return {"answer": answer}

# Explanation - POST API
@app.post("/explain")
async def explain_api(request: Request):
    data = await request.json()
    topic = data.get("topic")
    if not topic:
        return JSONResponse(content={"error": "Please provide a topic."}, status_code=400)
    explanation = explain_topic(topic)
    return {"topic": topic, "explanation": explanation}

# Summarization - POST API
@app.post("/summarize")
async def summarize_api(request: Request):
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(content={"error": "Please provide text to summarize."}, status_code=400)
    summary = summarize_text(text)
    return {"summary": summary}

# Quiz Generation - POST API
@app.post("/quiz")
async def quiz_api(request: Request):
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(content={"error": "Please provide text for quiz."}, status_code=400)
    quiz = generate_quiz(text)
    print("Generated quiz:", quiz) # ✅ DEBUG
    return JSONResponse(content={"quiz": quiz})

# Learning Path - POST API
@app.post("/learning-path")
async def learning_path_api(request: Request):
    data = await request.json()
    topic = data.get("topic")
    if not topic:
        return JSONResponse(content={"error": "Please provide a topic."}, status_code=400)
    
    path_result = get_learning_recommendations(topic)
    return {"learning_path": path_result}