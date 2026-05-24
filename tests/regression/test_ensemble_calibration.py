from bpfense_ai import (
    BPFenseClient,
)

from tests.regression.replay_loader import (
    load_replay_sample,
)

# =========================================================
# CLIENT
# =========================================================

client = BPFenseClient()

client.load()

# =========================================================
# TEST ENSEMBLE OUTPUT
# =========================================================

def test_ensemble_output():

    sample = load_replay_sample(

        "tests/replay/benign/"
        "basic_user_activity.json"
    )

    result = client.predict(
        sample
    )

    assert result.backend == (
        "ensemble"
    )

    assert (
        0.0 <= result.score <= 1.0
    )

    assert (
        0.0 <= result.confidence <= 1.0
    )

# =========================================================
# TEST ENSEMBLE DETERMINISM
# =========================================================

def test_ensemble_determinism():

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

    assert (
        result_1.score
        == result_2.score
    )

    assert (
        result_1.confidence
        == result_2.confidence
    )
