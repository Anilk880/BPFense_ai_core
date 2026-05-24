"""
Canonical behavioral feature schema.

This file is the SINGLE source of truth for:

- TensorFlow training
- sklearn training
- inference runtimes
- preprocessing
- ONNX export
- dataset loading
- future ensemble systems

IMPORTANT:
Do NOT reorder existing features after models
have been trained and exported.

Adding new features must ONLY append fields.
"""

from typing import List

# =========================================================
# CANONICAL FEATURE ORDER
# =========================================================

FEATURE_COLUMNS: List[str] = [

    # =====================================================
    # EXECUTION FEATURES
    # =====================================================

    "exec_count",

    "shell_exec_count",

    "sensitive_binary_execs",

    # =====================================================
    # NETWORK FEATURES
    # =====================================================

    "net_count",

    "dns_requests",

    "external_connections",

    "unique_ips",

    "unique_ports",

    # =====================================================
    # CORRELATION FEATURES
    # =====================================================

    "exec_net_ratio",

    "activity_ratio",

    # =====================================================
    # BEHAVIORAL FEATURES
    # =====================================================

    "burst",

    "behavior_entropy",

    "event_density",

    # =====================================================
    # SEQUENCE FEATURES
    # =====================================================

    "sequence_score",

    # =====================================================
    # STATISTICAL FEATURES
    # =====================================================

    "avg_exec_drift",

    "avg_net_drift",

    # =====================================================
    # TEMPORAL FEATURES
    # =====================================================

    "time_delta_variance",
]

# =========================================================
# FEATURE DIMENSION
# =========================================================

FEATURE_DIMENSION = len(
    FEATURE_COLUMNS
)

# =========================================================
# FEATURE VERSION
# =========================================================

FEATURE_SCHEMA_VERSION = "v1"

# =========================================================
# IMMUTABLE FEATURE INDEX MAP
# =========================================================

FEATURE_INDEX = {

    name: index

    for index, name in enumerate(
        FEATURE_COLUMNS
    )
}
