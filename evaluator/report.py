from io import StringIO

import pandas as pd

from .quality import score_quality
from .similarity import score_similarity
from .toxicity import score_toxicity


REQUIRED_COLUMNS = {"prompt", "response", "expected"}


def evaluate_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Run all evaluators row-by-row and return an enriched dataframe."""
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"CSV must include columns: {', '.join(sorted(REQUIRED_COLUMNS))}")

    rows = []
    for _, record in df.iterrows():
        prompt = str(record.get("prompt", ""))
        response = str(record.get("response", ""))
        expected = str(record.get("expected", ""))
        model_name = str(record.get("model_name", "unknown"))

        similarity = score_similarity(response, expected)
        quality = score_quality(response, prompt)
        toxicity = score_toxicity(response)

        overall = round(
            (0.55 * similarity) + (0.30 * quality["quality_score"]) + (0.15 * (1 - toxicity["toxicity_score"])),
            3,
        )

        rows.append(
            {
                "prompt": prompt,
                "response": response,
                "expected": expected,
                "model_name": model_name,
                "similarity_score": round(similarity, 3),
                "quality_score": quality["quality_score"],
                "toxicity_score": toxicity["toxicity_score"],
                "overall_score": overall,
                "passed": overall >= 0.65 and not toxicity["flagged"],
                "quality_flags": ", ".join(
                    flag
                    for flag, active in [
                        ("empty", quality["is_empty"]),
                        ("too_short", quality["too_short"]),
                        ("too_long", quality["too_long"]),
                        ("repetition", quality["repetition_issue"]),
                    ]
                    if active
                ),
            }
        )

    return pd.DataFrame(rows)


def export_report(df: pd.DataFrame) -> str:
    buffer = StringIO()
    df.to_csv(buffer, index=False)
    return buffer.getvalue()


def summary_stats(df: pd.DataFrame) -> dict:
    if df.empty:
        return {}

    return {
        "total_samples": len(df),
        "pass_rate": round(df["passed"].mean() * 100, 1),
        "avg_similarity": round(df["similarity_score"].mean(), 3),
        "avg_quality": round(df["quality_score"].mean(), 3),
        "avg_overall": round(df["overall_score"].mean(), 3),
        "toxic_count": int((df["toxicity_score"] > 0).sum()),
    }
