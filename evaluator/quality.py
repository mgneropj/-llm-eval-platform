import re


def score_quality(response: str, prompt: str = "") -> dict:
    """Basic response quality checks without external APIs."""
    text = (response or "").strip()
    words = text.split()

    empty = len(text) == 0
    too_short = len(words) < 5
    too_long = len(words) > 500

    repeated_tokens = 0
    if words:
        counts = {}
        for word in words:
            key = word.lower()
            counts[key] = counts.get(key, 0) + 1
        repeated_tokens = sum(1 for count in counts.values() if count >= 4)

    has_placeholder = bool(
        re.search(r"\b(as an ai|i cannot|i can't help|placeholder|lorem ipsum)\b", text, re.I)
    )

    prompt_words = set(re.findall(r"\w+", (prompt or "").lower()))
    response_words = set(re.findall(r"\w+", text.lower()))
    overlap = len(prompt_words & response_words) / max(len(prompt_words), 1)

    penalties = sum(
        [
            0.35 if empty else 0.0,
            0.20 if too_short else 0.0,
            0.10 if too_long else 0.0,
            0.15 if repeated_tokens >= 3 else 0.0,
            0.15 if has_placeholder else 0.0,
        ]
    )

    score = max(0.0, 1.0 - penalties)
    return {
        "quality_score": round(score, 3),
        "is_empty": empty,
        "too_short": too_short,
        "too_long": too_long,
        "repetition_issue": repeated_tokens >= 3,
        "prompt_overlap": round(overlap, 3),
    }
