from fastapi import FastAPI, File, UploadFile, HTTPException
from app.parser import extract_text
from app.analyzer import analyze_resume
from app.ai_detector import ai_probability
from app.review import generate_review

app = FastAPI(title="CV Analyzer Backend")


@app.get("/")
def root():
    return {"status": "Backend is running"}


@app.post("/analyze-cv")
async def analyze_cv(file: UploadFile = File(...)):

    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX files allowed")

    text = extract_text(file)

    if len(text.strip()) < 100:
        raise HTTPException(status_code=400, detail="CV content too short")

    scores = analyze_resume(text)
    ai_score = ai_probability(text)

    final_score = round(
        scores["impact"] * 0.4 +
        scores["skills"] * 0.25 +
        scores["experience"] * 0.2 +
        ai_score * 0.15
    )

    review = generate_review(final_score)

    return {
        "final_score": final_score,
        "ai_usage_probability": ai_score,
        "scores": scores,
        "review": review
    }
