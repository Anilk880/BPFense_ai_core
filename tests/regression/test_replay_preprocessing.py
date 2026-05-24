import pytest
import numpy as np

from bpfense_ai.preprocessing.preprocessor import (
    preprocess_features,
)

from bpfense_ai.preprocessing.exceptions import (
    FeatureValidationError,
)

from bpfense_ai.inference.common.feature_schema import (
    FEATURE_DIMENSION,
)

from bpfense_ai.testing.replay_loader import (
    load_replay_sample,
)

# =========================================================
# BENIGN REPLAY TEST
# =========================================================

def test_benign_replay():

    sample = load_replay_sample(

        "tests/replay/benign/"
        "basic_user_activity.json"
    )

    vector = preprocess_features(
        sample
    )

    assert isinstance(
        vector,
        np.ndarray
    )

    assert len(vector) == (
        FEATURE_DIMENSION
    )

# =========================================================
# MALICIOUS REPLAY TEST
# =========================================================

def test_malicious_replay():

    sample = load_replay_sample(

        "tests/replay/malicious/"
        "reverse_shell_activity.json"
    )

    vector = preprocess_features(
        sample
    )

    assert isinstance(
        vector,
        np.ndarray
    )

    assert len(vector) == (
        FEATURE_DIMENSION
    )

# =========================================================
# MALFORMED REPLAY TEST
# =========================================================

def test_malformed_replay():

    sample = load_replay_sample(

        "tests/replay/malformed/"
        "nan_payload.json"
    )

    with pytest.raises(
        FeatureValidationError
    ):

        preprocess_features(
            sample
        )
