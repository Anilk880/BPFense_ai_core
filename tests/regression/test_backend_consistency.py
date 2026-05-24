from bpfense_ai.inference._tensorflow import (
    TensorFlowRuntime,
)

from bpfense_ai.inference._sklearn import (
    SklearnRuntime,
)

from bpfense_ai.configs.settings import (
    TF_MODEL_PATH,
    SKLEARN_MODEL_PATH,
)

from bpfense_ai.testing.replay_loader import (
    load_replay_sample,
)

# =========================================================
# LOAD RUNTIMES
# =========================================================

tf_runtime = TensorFlowRuntime(
    str(TF_MODEL_PATH)
)

sk_runtime = SklearnRuntime(
    str(SKLEARN_MODEL_PATH)
)

# =========================================================
# LOAD MODELS
# =========================================================

tf_runtime.load()

sk_runtime.load()

# =========================================================
# TEST BENIGN BACKEND CONSISTENCY
# =========================================================

def test_benign_backend_consistency():

    sample = load_replay_sample(

        "tests/replay/benign/"
        "basic_user_activity.json"
    )

    tf_result = tf_runtime.predict(
        sample
    )

    sk_result = sk_runtime.predict(
        sample
    )

    # =====================================================
    # SCORE VALIDATION
    # =====================================================

    assert (
        0.0 <= tf_result.score <= 1.0
    )

    assert (
        0.0 <= sk_result.score <= 1.0
    )

    # =====================================================
    # LABEL VALIDATION
    # =====================================================

    assert tf_result.label in [

        "normal",

        "malicious",
    ]

    assert sk_result.label in [

        "normal",

        "malicious",
    ]

# =========================================================
# TEST MALICIOUS BACKEND CONSISTENCY
# =========================================================

def test_malicious_backend_consistency():

    sample = load_replay_sample(

        "tests/replay/malicious/"
        "reverse_shell_activity.json"
    )

    tf_result = tf_runtime.predict(
        sample
    )

    sk_result = sk_runtime.predict(
        sample
    )

    # =====================================================
    # SCORE VALIDATION
    # =====================================================

    assert (
        0.0 <= tf_result.score <= 1.0
    )

    assert (
        0.0 <= sk_result.score <= 1.0
    )

    # =====================================================
    # LABEL VALIDATION
    # =====================================================

    assert tf_result.label in [

        "normal",

        "malicious",
    ]

    assert sk_result.label in [

        "normal",

        "malicious",
    ]

# =========================================================
# TEST BACKEND DETERMINISM
# =========================================================

def test_backend_determinism():

    sample = load_replay_sample(

        "tests/replay/benign/"
        "basic_user_activity.json"
    )

    tf_result_1 = tf_runtime.predict(
        sample
    )

    tf_result_2 = tf_runtime.predict(
        sample
    )

    sk_result_1 = sk_runtime.predict(
        sample
    )

    sk_result_2 = sk_runtime.predict(
        sample
    )

    # =====================================================
    # TENSORFLOW DETERMINISM
    # =====================================================

    assert (
        tf_result_1.score
        == tf_result_2.score
    )

    assert (
        tf_result_1.label
        == tf_result_2.label
    )

    # =====================================================
    # SKLEARN DETERMINISM
    # =====================================================

    assert (
        sk_result_1.score
        == sk_result_2.score
    )

    assert (
        sk_result_1.label
        == sk_result_2.label
    )
