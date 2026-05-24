# =========================================================
# BASE API ERROR
# =========================================================

class BPFenseError(Exception):
    """
    Base BPFense exception.
    """
    pass

# =========================================================
# VALIDATION ERROR
# =========================================================

class ValidationError(
    BPFenseError
):
    """
    Raised when request validation fails.
    """
    pass

# =========================================================
# MODEL LOAD ERROR
# =========================================================

class ModelLoadError(
    BPFenseError
):
    """
    Raised when a model fails to load.
    """
    pass

# =========================================================
# MODEL NOT LOADED
# =========================================================

class ModelNotLoadedError(
    BPFenseError
):
    """
    Raised when inference is attempted
    before models are loaded.
    """
    pass

# =========================================================
# INFERENCE ERROR
# =========================================================

class InferenceError(
    BPFenseError
):
    """
    Raised when inference fails.
    """
    pass
