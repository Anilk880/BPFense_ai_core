import joblib

from bpfense_ai.preprocessing.preprocessor import (
    preprocess_features,
)

from bpfense_ai.inference.common.interfaces import (
    InferenceBackend,
)

from bpfense_ai.inference.common.types import (
    PredictionResult,
)


class SklearnRuntime(InferenceBackend):

    def __init__(self, model_path: str):

        self.model_path = model_path

        self.model = None

    def load(self):

        bundle = joblib.load(
            self.model_path
        )

        self.model = bundle["model"]

    def predict(self, features):

        processed = preprocess_features(
            features
        )

        prediction = self.model.predict(
            [processed]
        )[0]

        score = (
            1.0
            if prediction == -1
            else 0.0
        )

        label = (
            "malicious"
            if prediction == -1
            else "normal"
        )

        severity = (
            "high"
            if prediction == -1
            else "low"
        )

        return PredictionResult(

            backend="sklearn",

            label=label,

            score=score,

            severity=severity,

            raw_output=prediction
        )

    def healthy(self) -> bool:

        return self.model is not None
