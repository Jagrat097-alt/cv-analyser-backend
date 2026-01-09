def generate_review(score: int):
    if score >= 80:
        return {
            "summary": "Excellent CV with strong structure and clear impact.",
            "strengths": [
                "Good use of measurable results",
                "Clear technical skills",
                "Relevant experience"
            ],
            "improvements": [
                "Minor formatting improvements",
                "Customize CV for specific job roles"
            ]
        }

    if score >= 50:
        return {
            "summary": "Good CV but lacks strong measurable impact.",
            "strengths": [
                "Relevant skills mentioned",
                "Some experience or projects included"
            ],
            "improvements": [
                "Add numbers to achievements",
                "Explain how skills were used",
                "Make project outcomes clearer"
            ]
        }

    return {
        "summary": "CV needs significant improvement.",
        "strengths": [
            "Basic structure present"
        ],
        "improvements": [
            "Add projects or internships",
            "Quantify your work using numbers",
            "Avoid generic descriptions",
            "Clearly list technical skills"
        ]
    }
