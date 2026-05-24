import pytest

from bpfense_ai import (
    BPFenseClient,
)

from bpfense_ai.testing.replay_loader import (
    load_replay_sample,
)

# =========================================================
# CLIENT
# =========================================================

client = BPFenseClient()

# =========================================================
# LOAD MODELS
# =========================================================

client.load()

# =========================================================
# TEST BENIGN INFERENCE
# =========================================================

def test_benign_inference():

    sample = load_replay_sample(

        "tests/replay/benign/"
        "basic_user_activity.json"
    )

    result = client.predict(
        sample
    )

    # =====================================================
    # BASIC RESPONSE VALIDATION
    # =====================================================

    assert result.label in [

        "normal",

        "malicious",
    ]

    assert result.severity in [

        "low",

        "medium",

        "high",

        "critical",
    ]

    assert isinstance(
        result.score,
        float
    )

    # =====================================================
    # SCORE RANGE VALIDATION
    # =====================================================

    assert (
        0.0 <= result.score <= 1.0
    )

# =========================================================
# TEST MALICIOUS INFERENCE
# =========================================================

def test_malicious_inference():

    sample = load_replay_sample(

        "tests/replay/malicious/"
        "reverse_shell_activity.json"
    )

    result = client.predict(
        sample
    )

    # =====================================================
    # RESPONSE VALIDATION
    # =====================================================

    assert result.label in [

        "normal",

        "malicious",
    ]

    assert result.severity in [

        "low",

        "medium",

        "high",

        "critical",
    ]

    assert isinstance(
        result.score,
        float
    )

    # =====================================================
    # SCORE RANGE VALIDATION
    # =====================================================

    assert (
        0.0 <= result.score <= 1.0
    )

# =========================================================
# TEST DETERMINISTIC INFERENCE
# =========================================================

def test_deterministic_inference():

    sample = load_replay_sample(

        "tests/replay/benign/"
        "basic_user_activity.json"
    )

    result_1 = client.predict(
        sample
    )

    result_2 = client.predict(
        sample
    )

    # =====================================================
    # DETERMINISTIC SCORE CHECK
    # =====================================================

    assert (
        result_1.score
        == result_2.score
    )

    assert (
        result_1.label
        == result_2.label
    )

    assert (
        result_1.severity
        == result_2.severity
    )
