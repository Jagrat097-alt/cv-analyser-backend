import statistics


def ai_probability(text: str) -> int:
    """
    Returns a small score (0–15) representing AI-likeness.
    Lower is better (more human-like).
    """

    sentences = [s.strip() for s in text.split(".") if len(s.strip()) > 5]

    if len(sentences) < 5:
        return 5

    lengths = [len(s.split()) for s in sentences]

    try:
        variation = statistics.pstdev(lengths)
    except statistics.StatisticsError:
        return 5

    if variation < 3:
        return 15
    elif variation < 6:
        return 10
    else:
        return 5
