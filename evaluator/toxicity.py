import re

TOXIC_PATTERNS = [
    r"\b(kill yourself|kys|hate you|stupid idiot|shut up)\b",
    r"\b(racist|sexist|abuse|harass)\b",
    r"\b(f[\*]?ck|sh[\*]?t|bitch|bastard)\b",
]


def score_toxicity(text: str) -> dict:
    """Lightweight toxicity screening for MVP deployments."""
    content = (text or "").strip().lower()
    if not content:
        return {"toxicity_score": 0.0, "flagged": False, "matched_rules": []}

    matched = [pattern for pattern in TOXIC_PATTERNS if re.search(pattern, content, re.I)]
    score = min(1.0, 0.25 * len(matched))
    return {
        "toxicity_score": round(score, 3),
        "flagged": score >= 0.25,
        "matched_rules": matched,
    }
