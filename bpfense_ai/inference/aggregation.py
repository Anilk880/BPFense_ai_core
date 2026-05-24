from typing import List

from bpfense_ai.inference.common.types import (
    PredictionResult,
)

# =========================================================
# BACKEND WEIGHTS
# =========================================================

BACKEND_WEIGHTS = {

    "tensorflow": 0.4,

    "sklearn": 0.6,
}

# =========================================================
# WEIGHTED SCORE
# =========================================================

def weighted_score(
    results: List[PredictionResult]
) -> float:

    weighted_total = 0.0

    total_weight = 0.0

    for result in results:

        weight = BACKEND_WEIGHTS.get(

            result.backend,

            0.0
        )

        weighted_total += (
            result.score * weight
        )

        total_weight += weight

    if total_weight == 0:

        return 0.0

    return round(

        weighted_total / total_weight,

        6
    )

# =========================================================
# FINAL LABEL
# =========================================================

def aggregate_label(
    score: float
) -> str:

    return (

        "malicious"

        if score >= 0.5

        else "normal"
    )

# =========================================================
# SEVERITY
# =========================================================

def aggregate_severity(
    score: float
) -> str:

    if score >= 0.9:
        return "critical"

    if score >= 0.7:
        return "high"

    if score >= 0.5:
        return "medium"

    return "low"
