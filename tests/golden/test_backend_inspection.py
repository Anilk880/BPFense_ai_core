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

tf_runtime.load()
sk_runtime.load()

# =========================================================
# BENIGN INSPECTION
# =========================================================

def test_benign_backend_scores():

    sample = load_replay_sample(

        "tests/golden/benign/"
        "normal_terminal_usage.json"
    )

    tf_result = tf_runtime.predict(
        sample
    )

    sk_result = sk_runtime.predict(
        sample
    )

    print("\nTensorFlow:")
    print(tf_result)

    print("\nSklearn:")
    print(sk_result)

# =========================================================
# MALICIOUS INSPECTION
# =========================================================

def test_malicious_backend_scores():

    sample = load_replay_sample(

        "tests/golden/malicious/"
        "reverse_shell.json"
    )

    tf_result = tf_runtime.predict(
        sample
    )

    sk_result = sk_runtime.predict(
        sample
    )

    print("\nTensorFlow:")
    print(tf_result)

    print("\nSklearn:")
    print(sk_result)
