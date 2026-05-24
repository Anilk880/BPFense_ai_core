from typing import Dict
from typing import Any

import numpy as np

from bpfense_ai.inference.common.feature_schema import (
    FEATURE_COLUMNS,
    FEATURE_DIMENSION,
)

# =========================================================
# CANONICAL NORMALIZATION RANGES
# =========================================================
#
# IMPORTANT:
# These ranges MUST remain aligned with:
#
# - telemetry distributions
# - training datasets
# - runtime inference
# - exported TensorFlow models
# - future ONNX runtimes
#
# Updating ranges after training requires
# model retraining.
# =========================================================

NORMALIZATION_RANGES = {

    # =====================================================
    # EXECUTION FEATURES
    # =====================================================

    "exec_count": 100.0,

    "shell_exec_count": 20.0,

    "sensitive_binary_execs": 20.0,

    # =====================================================
    # NETWORK FEATURES
    # =====================================================

    "net_count": 50.0,

    "dns_requests": 100.0,

    "external_connections": 50.0,

    "unique_ips": 25.0,

    "unique_ports": 50.0,

    # =====================================================
    # CORRELATION FEATURES
    # =====================================================

    "exec_net_ratio": 20.0,

    "activity_ratio": 20.0,

    # =====================================================
    # BEHAVIORAL FEATURES
    # =====================================================

    "burst": 50.0,

    "behavior_entropy": 10.0,

    "event_density": 10.0,

    # =====================================================
    # SEQUENCE FEATURES
    # =====================================================

    "sequence_score": 100.0,

    # =====================================================
    # STATISTICAL FEATURES
    # =====================================================

    "avg_exec_drift": 100.0,

    "avg_net_drift": 100.0,

    # =====================================================
    # TEMPORAL FEATURES
    # =====================================================

    "time_delta_variance": 100.0,
}

# =========================================================
# FEATURE PREPROCESSOR
# =========================================================

class FeaturePreprocessor:
    """
    Canonical behavioral feature preprocessor.

    Responsibilities:
    - enforce immutable feature ordering
    - normalize behavioral telemetry
    - construct inference/training vectors
    - guarantee tensor consistency

    Used by:
    - TensorFlow training
    - sklearn training
    - inference runtimes
    - future ONNX runtime
    """

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        self.ranges = NORMALIZATION_RANGES

        self.feature_columns = FEATURE_COLUMNS

        self.feature_dimension = FEATURE_DIMENSION

    # =====================================================
    # NORMALIZE SINGLE FEATURE
    # =====================================================

    def normalize_feature(

        self,

        feature_name: str,

        value: Any

    ) -> float:

        max_value = self.ranges.get(
            feature_name,
            1.0
        )

        try:

            normalized = (
                float(value) / max_value
            )

        except Exception:

            normalized = 0.0

        normalized = max(
            0.0,
            min(normalized, 1.0)
        )

        return round(
            normalized,
            6
        )

    # =====================================================
    # TRANSFORM FEATURE DICT
    # =====================================================

    def transform(
        self,
        features: Dict[str, Any]
    ) -> np.ndarray:

        vector = []

        for feature_name in self.feature_columns:

            value = features.get(
                feature_name,
                0.0
            )

            normalized = self.normalize_feature(

                feature_name,

                value
            )

            vector.append(normalized)

        vector = np.array(
            vector,
            dtype=np.float32
        )

        # =================================================
        # DIMENSION SAFETY CHECK
        # =================================================

        if len(vector) != self.feature_dimension:

            raise ValueError(

                "Feature dimension mismatch: "

                f"expected={self.feature_dimension} "

                f"got={len(vector)}"
            )

        return vector

    # =====================================================
    # FEATURE NAMES
    # =====================================================

    def feature_names(self):

        return list(
            self.feature_columns
        )

    # =====================================================
    # FEATURE COUNT
    # =====================================================

    def dimension(self):

        return self.feature_dimension

# =========================================================
# GLOBAL PREPROCESSOR INSTANCE
# =========================================================

_preprocessor = FeaturePreprocessor()

# =========================================================
# LEGACY / RUNTIME WRAPPER
# =========================================================

def preprocess_features(features):

    return _preprocessor.transform(
        features
    )
