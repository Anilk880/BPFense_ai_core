from typing import Optional

from bpfense_ai.api.schemas import (
    PredictionRequest,
    PredictionResponse,
)

from bpfense_ai.api.exceptions import (
    ModelNotLoadedError,
    InferenceError,
    ValidationError,
)

from bpfense_ai.inference.classifier import (
    BehavioralClassifier,
)

from bpfense_ai.inference._tensorflow.runtime import (
    TensorFlowRuntime,
)

from bpfense_ai.inference._sklearn.runtime import (
    SklearnRuntime,
)

from bpfense_ai.configs.settings import (
    TF_MODEL_PATH,
    SKLEARN_MODEL_PATH,
)

from bpfense_ai.preprocessing.preprocessor import (
    preprocess_features,
)

from bpfense_ai.preprocessing.exceptions import (
    FeatureValidationError,
)

# =========================================================
# BPFENSE CLIENT
# =========================================================

class BPFenseClient:
    """
    Production-grade behavioral ML inference client.
    """

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        self.loaded = False

        self.classifier: Optional[
            BehavioralClassifier
        ] = None

    # =====================================================
    # LOAD MODELS
    # =====================================================

    def load(self):

        tf_runtime = TensorFlowRuntime(
            str(TF_MODEL_PATH)
        )

        sk_runtime = SklearnRuntime(
            str(SKLEARN_MODEL_PATH)
        )

        self.classifier = (
            BehavioralClassifier(
                backends=[
                    tf_runtime,
                    sk_runtime,
                ]
            )
        )

        self.classifier.load()

        self.loaded = True

    # =====================================================
    # HEALTH CHECK
    # =====================================================

    def health(self):

        return {

            "healthy": self.loaded
        }

    # =====================================================
    # PREDICT
    # =====================================================

    def predict(
        self,
        features,
    ) -> PredictionResponse:

        # ================================================
        # VALIDATE INPUT FIRST
        # ================================================

        try:

            preprocess_features(
                features
            )

        except FeatureValidationError as e:

            raise ValidationError(
                str(e)
            )

        # ================================================
        # LAZY MODEL LOADING
        # ================================================

        if not self.loaded:

            self.load()

        # ================================================
        # RUN INFERENCE
        # ================================================

        try:

            request = PredictionRequest(
                features=features
            )

            result = self.classifier.predict(
                request.features
            )

            return PredictionResponse(

                label=result["label"],

                severity=result["severity"],

                score=float(
                    result["score"]
                ),

                confidence=float(
                    result["confidence"]
                ),

                backend=result["backend"],
            )

        except ValidationError:
            raise

        except Exception as e:

            raise InferenceError(

                f"inference failed: {e}"
            )
