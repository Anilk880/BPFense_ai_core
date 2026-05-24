from typing import List

from bpfense_ai.inference.common.types import (
    PredictionResult,
)

from bpfense_ai.inference.aggregation import (
    weighted_score,
    aggregate_label,
    aggregate_severity,
)

from bpfense_ai.inference.confidence import (
    confidence_score,
)

# =========================================================
# ENSEMBLE CLASSIFIER
# =========================================================

class BehavioralClassifier:

    def __init__(
        self,
        backends: List
    ):

        self.backends = backends

    # =====================================================
    # LOAD BACKENDS
    # =====================================================

    def load(self):

        for backend in self.backends:

            backend.load()

    # =====================================================
    # PREDICT
    # =====================================================

    def predict(
        self,
        features
    ):

        results = []

        for backend in self.backends:

            result = backend.predict(
                features
            )

            results.append(
                result
            )

        return self._aggregate(
            results
        )

    # =====================================================
    # AGGREGATE
    # =====================================================

    def _aggregate(
        self,
        results: List[PredictionResult]
    ):

        ensemble_score = weighted_score(
            results
        )

        label = aggregate_label(
            ensemble_score
        )

        severity = aggregate_severity(
            ensemble_score
        )

        confidence = confidence_score(
            results
        )

        return {

            "label": label,

            "severity": severity,

            "score": ensemble_score,

            "confidence": confidence,

            "backend": "ensemble",

            "results": results,
        }
