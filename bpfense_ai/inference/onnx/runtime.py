import onnxruntime as ort
import numpy as np

from bpfense_ai.preprocessing.preprocessor import preprocess_features
from bpfense_ai.inference.common.interfaces import InferenceBackend
from bpfense_ai.inference.common.types import PredictionResult


class ONNXRuntime(InferenceBackend):

    def __init__(self, model_path: str):
        self.model_path = model_path
        self.session = None

    def load(self):
        self.session = ort.InferenceSession(self.model_path)

    def predict(self, features):

        processed = preprocess_features(features)

        input_name = self.session.get_inputs()[0].name

        outputs = self.session.run(
            None,
            {
                input_name: np.array([processed], dtype=np.float32)
            }
        )

        score = float(outputs[0][0][0])

        label = "malicious" if score >= 0.5 else "normal"

        severity = "high" if score >= 0.7 else "low"

        return PredictionResult(
            backend="onnx",
            label=label,
            score=score,
            severity=severity,
            raw_output=outputs
        )

    def healthy(self) -> bool:
        return self.session is not None
