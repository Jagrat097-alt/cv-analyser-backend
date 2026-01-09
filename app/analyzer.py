import re
import spacy

# Load NLP model once
nlp = spacy.load("en_core_web_sm")


def analyze_resume(text: str):
    text_lower = text.lower()
    doc = nlp(text_lower)

    # ---------------------------
    # 1. Impact score (numbers, metrics)
    # ---------------------------
    metrics = re.findall(r"\d+%|\d+\+|\$\d+", text)
    impact_score = min(len(metrics) * 5, 40)

    # ---------------------------
    # 2. Skills score
    # ---------------------------
    skill_keywords = [
        "python", "java", "c++", "c", "sql",
        "machine learning", "ml", "ai",
        "fastapi", "django", "flask",
        "javascript", "react"
    ]

    skills_found = set()
    for skill in skill_keywords:
        if skill in text_lower:
            skills_found.add(skill)

    skills_score = min(len(skills_found) * 4, 25)

    # ---------------------------
    # 3. Experience score
    # ---------------------------
    experience_keywords = [
        "intern", "internship", "engineer",
        "developer", "worked", "company",
        "organization", "role", "project"
    ]

    experience_hits = sum(1 for word in experience_keywords if word in text_lower)
    experience_score = min(experience_hits * 3, 20)

    return {
        "impact": impact_score,
        "skills": skills_score,
        "experience": experience_score
    }
