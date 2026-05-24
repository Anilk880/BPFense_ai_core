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

# =========================================================
# VALID FEATURES
# =========================================================

VALID_FEATURES = {

    "exec_count": 5,

    "shell_exec_count": 1,

    "net_count": 2,

    "dns_requests": 1,
}

# =========================================================
# TEST VALID PREPROCESSING
# =========================================================

def test_preprocessing_success():

    vector = preprocess_features(
        VALID_FEATURES
    )

    assert isinstance(
        vector,
        np.ndarray
    )

    assert len(vector) == (
        FEATURE_DIMENSION
    )

# =========================================================
# TEST INVALID TYPE
# =========================================================

def test_invalid_type():

    with pytest.raises(
        FeatureValidationError
    ):

        preprocess_features(
            "invalid"
        )

# =========================================================
# TEST EMPTY FEATURES
# =========================================================

def test_empty_features():

    with pytest.raises(
        FeatureValidationError
    ):

        preprocess_features({})

# =========================================================
# TEST NAN REJECTION
# =========================================================

def test_nan_rejection():

    with pytest.raises(
        FeatureValidationError
    ):

        preprocess_features({

            "exec_count":
                float("nan")
        })

# =========================================================
# TEST INF REJECTION
# =========================================================

def test_inf_rejection():

    with pytest.raises(
        FeatureValidationError
    ):

        preprocess_features({

            "exec_count":
                float("inf")
        })

# =========================================================
# TEST RANGE VALIDATION
# =========================================================

def test_range_validation():

    with pytest.raises(
        FeatureValidationError
    ):

        preprocess_features({

            "exec_count":
                999999999
        })
