from functools import lru_cache

import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


@lru_cache(maxsize=1)
def _load_model() -> SentenceTransformer:
    return SentenceTransformer("all-MiniLM-L6-v2")


def score_similarity(response: str, expected: str) -> float:
    """Return cosine similarity (0-1) between response and expected answer."""
    response = (response or "").strip()
    expected = (expected or "").strip()

    if not response or not expected:
        return 0.0

    model = _load_model()
    embeddings = model.encode([response, expected])
    similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return float(np.clip(similarity, 0.0, 1.0))
