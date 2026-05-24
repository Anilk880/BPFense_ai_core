from typing import Dict
from typing import Any

from bpfense_ai.inference.classifier import (
    BehavioralClassifier,
)

from bpfense_ai.inference._tensorflow import (
    TensorFlowRuntime,
)

from bpfense_ai.inference._sklearn import (
    SklearnRuntime,
)

from bpfense_ai.api.schemas import (
    PredictionResponse,
)

from bpfense_ai.api.exceptions import (
    ValidationError,
)

from bpfense_ai.configs.settings import (
    TF_MODEL_PATH,
    SKLEARN_MODEL_PATH,
)


class BPFenseClient:

    def __init__(self):

        # =====================================
        # CREATE BACKEND ENGINES
        # =====================================

        backends = [

            TensorFlowRuntime(
                str(TF_MODEL_PATH)
            ),

            SklearnRuntime(
                str(SKLEARN_MODEL_PATH)
            ),
        ]

        # =====================================
        # CREATE CLASSIFIER
        # =====================================

        self.classifier = (
            BehavioralClassifier(
                backends
            )
        )

        self.loaded = False

    # =========================================
    # LOAD MODELS
    # =========================================

    def load(self):

        if not self.loaded:

            self.classifier.load()

            self.loaded = True

    # =========================================
    # HEALTH STATUS
    # =========================================

    def health(self):

        return {
            "healthy": self.loaded
        }

    # =========================================
    # VALIDATE FEATURES
    # =========================================

    def _validate_features(
        self,
        features: Dict[str, Any],
    ):

        if features is None:

            raise ValidationError(
                "features cannot be None"
            )

        if not isinstance(
            features,
            dict,
        ):

            raise ValidationError(
                "features must be a dictionary"
            )

        if len(features) == 0:

            raise ValidationError(
                "features cannot be empty"
            )

    # =========================================
    # PREDICT
    # =========================================

    def predict(
        self,
        features: Dict[str, Any],
    ) -> PredictionResponse:

        # =====================================
        # VALIDATE INPUT
        # =====================================

        self._validate_features(
            features
        )

        # =====================================
        # LOAD MODELS
        # =====================================

        self.load()

        # =====================================
        # RUN INFERENCE
        # =====================================

        result = self.classifier.predict(
            features
        )

        # =====================================
        # NORMALIZE RESPONSE
        # =====================================

        return PredictionResponse(

            label=result["label"],

            severity=result["severity"],

            score=float(
                result["score"]
            ),

            backend=result["backend"],
        )
