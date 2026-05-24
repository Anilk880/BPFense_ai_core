import math

from typing import Any
from typing import Dict

from bpfense_ai.preprocessing.exceptions import (
    FeatureValidationError,
)

# =========================================================
# FEATURE VALUE LIMITS
# =========================================================

FEATURE_LIMITS = {

    "exec_count": (0, 100000),

    "shell_exec_count": (0, 10000),

    "sensitive_binary_execs": (0, 10000),

    "net_count": (0, 100000),

    "dns_requests": (0, 100000),

    "external_connections": (0, 100000),

    "unique_ips": (0, 100000),

    "unique_ports": (0, 65535),

    "exec_net_ratio": (0.0, 1000.0),

    "activity_ratio": (0.0, 1000.0),

    "burst": (0.0, 1000.0),

    "behavior_entropy": (0.0, 100.0),

    "event_density": (0.0, 1000.0),

    "sequence_score": (0.0, 1000.0),

    "avg_exec_drift": (0.0, 1000.0),

    "avg_net_drift": (0.0, 1000.0),

    "time_delta_variance": (0.0, 1000.0),
}

# =========================================================
# VALIDATE NUMERIC VALUE
# =========================================================

def validate_numeric(
    feature_name: str,
    value: Any,
) -> float:

    try:

        numeric = float(value)

    except Exception:

        raise FeatureValidationError(

            f"feature '{feature_name}' "

            f"must be numeric"
        )

    if math.isnan(numeric):

        raise FeatureValidationError(

            f"feature '{feature_name}' "

            f"cannot be NaN"
        )

    if math.isinf(numeric):

        raise FeatureValidationError(

            f"feature '{feature_name}' "

            f"cannot be infinite"
        )

    return numeric

# =========================================================
# VALIDATE FEATURE RANGE
# =========================================================

def validate_range(
    feature_name: str,
    value: float,
):

    minimum, maximum = FEATURE_LIMITS.get(

        feature_name,

        (-1e12, 1e12)
    )

    if value < minimum:

        raise FeatureValidationError(

            f"feature '{feature_name}' "

            f"below minimum: {minimum}"
        )

    if value > maximum:

        raise FeatureValidationError(

            f"feature '{feature_name}' "

            f"above maximum: {maximum}"
        )

# =========================================================
# VALIDATE FEATURE DICTIONARY
# =========================================================

def validate_feature_dict(
    features: Dict[str, Any]
):

    if not isinstance(features, dict):

        raise FeatureValidationError(
            "features must be a dictionary"
        )

    if len(features) == 0:

        raise FeatureValidationError(
            "features cannot be empty"
        )

    for feature_name, value in features.items():

        numeric = validate_numeric(
            feature_name,
            value,
        )

        validate_range(
            feature_name,
            numeric,
        )
