from typing import List

from bpfense_ai.inference.common.types import (
    PredictionResult,
)

# =========================================================
# BACKEND AGREEMENT
# =========================================================

def backend_agreement(
    results: List[PredictionResult]
) -> float:

    labels = [

        result.label

        for result in results
    ]

    majority = max(

        set(labels),

        key=labels.count
    )

    agreement = (

        labels.count(majority)

        / len(labels)
    )

    return round(
        agreement,
        6
    )

# =========================================================
# CONFIDENCE SCORE
# =========================================================

def confidence_score(
    results: List[PredictionResult]
) -> float:

    agreement = backend_agreement(
        results
    )

    average_score = (

        sum(r.score for r in results)

        / len(results)
    )

    confidence = (
        agreement * average_score
    )

    return round(
        confidence,
        6
    )
