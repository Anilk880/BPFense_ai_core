from typing import List

from bpfense_ai.inference.common.types import PredictionResult


class BehavioralClassifier:

    def __init__(self, backends: List):
        self.backends = backends

    def load(self):

        for backend in self.backends:
            backend.load()

    def predict(self, features):

        results = []

        for backend in self.backends:
            results.append(backend.predict(features))

        return self._aggregate(results)

    def _aggregate(self, results):

        max_result = max(results, key=lambda r: r.score)

        return {
            "label": max_result.label,
            "severity": max_result.severity,
            "score": max_result.score,
            "backend": max_result.backend,
            "results": results
        }
