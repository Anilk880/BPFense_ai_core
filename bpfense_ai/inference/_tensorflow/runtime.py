import tensorflow as tf

from bpfense_ai.preprocessing.preprocessor import preprocess_features
from bpfense_ai.inference.common.interfaces import InferenceBackend
from bpfense_ai.inference.common.types import PredictionResult


class TensorFlowRuntime(InferenceBackend):

    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = None

    def load(self):
        self.model = tf.saved_model.load(self.model_path)

    def predict(self, features):

        processed = preprocess_features(features)

        infer = self.model.signatures["serving_default"]

        tensor_input = tf.convert_to_tensor([processed], dtype=tf.float32)

        outputs = infer(tensor_input)

        score = float(list(outputs.values())[0][0][0])

        label = "malicious" if score >= 0.5 else "normal"

        severity = self._severity(score)

        return PredictionResult(
            backend="tensorflow",
            label=label,
            score=score,
            severity=severity,
            raw_output=outputs
        )

    def healthy(self) -> bool:
        return self.model is not None

    @staticmethod
    def _severity(score: float) -> str:

        if score >= 0.9:
            return "critical"

        if score >= 0.7:
            return "high"

        if score >= 0.5:
            return "medium"

        return "low"
