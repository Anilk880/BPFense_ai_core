from typing import Dict
from typing import Any

import numpy as np

from bpfense_ai.inference.common.feature_schema import (
    FEATURE_COLUMNS,
    FEATURE_DIMENSION,
)

from bpfense_ai.preprocessing.validators import (
    validate_feature_dict,
)

from bpfense_ai.preprocessing.normalization import (
    NORMALIZATION_RANGES,
)

from bpfense_ai.preprocessing.exceptions import (
    FeatureNormalizationError,
)

# =========================================================
# FEATURE PREPROCESSOR
# =========================================================

class FeaturePreprocessor:
    """
    Production-grade behavioral feature preprocessor.

    Responsibilities:
    - strict feature validation
    - deterministic normalization
    - immutable feature ordering
    - tensor dimension safety
    - runtime integrity guarantees
    """

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        self.columns = FEATURE_COLUMNS

        self.dimension = FEATURE_DIMENSION

        self.ranges = NORMALIZATION_RANGES

    # =====================================================
    # NORMALIZE FEATURE
    # =====================================================

    def normalize(
        self,
        feature_name: str,
        value: float,
    ) -> float:

        maximum = self.ranges.get(
            feature_name,
            1.0
        )

        # =================================================
        # NORMALIZATION SAFETY
        # =================================================

        if maximum <= 0:

            raise FeatureNormalizationError(

                f"invalid normalization range "

                f"for feature '{feature_name}'"
            )

        try:

            normalized = value / maximum

        except Exception as e:

            raise FeatureNormalizationError(

                f"failed to normalize "

                f"feature '{feature_name}': {e}"
            )

        # =================================================
        # CLAMP TO SAFE RANGE
        # =================================================

        normalized = max(
            0.0,
            min(normalized, 1.0)
        )

        return round(
            float(normalized),
            6
        )

    # =====================================================
    # TRANSFORM FEATURES
    # =====================================================

    def transform(
        self,
        features: Dict[str, Any],
    ) -> np.ndarray:

        # =================================================
        # STRICT VALIDATION
        # =================================================

        validate_feature_dict(
            features
        )

        vector = []

        # =================================================
        # IMMUTABLE FEATURE ORDER
        # =================================================

        for feature_name in self.columns:

            raw_value = features.get(
                feature_name,
                0.0
            )

            normalized = self.normalize(

                feature_name,

                float(raw_value)
            )

            vector.append(
                normalized
            )

        # =================================================
        # BUILD NUMPY VECTOR
        # =================================================

        vector = np.array(

            vector,

            dtype=np.float32
        )

        # =================================================
        # DIMENSION SAFETY
        # =================================================

        if len(vector) != self.dimension:

            raise ValueError(

                "feature dimension mismatch: "

                f"expected={self.dimension} "

                f"got={len(vector)}"
            )

        return vector

    # =====================================================
    # FEATURE NAMES
    # =====================================================

    def feature_names(self):

        return list(
            self.columns
        )

    # =====================================================
    # FEATURE DIMENSION
    # =====================================================

    def feature_dimension(self):

        return self.dimension

# =========================================================
# GLOBAL PREPROCESSOR INSTANCE
# =========================================================

_preprocessor = FeaturePreprocessor()

# =========================================================
# RUNTIME WRAPPER
# =========================================================

def preprocess_features(
    features: Dict[str, Any]
):

    return _preprocessor.transform(
        features
    )
