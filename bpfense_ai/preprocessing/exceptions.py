class PreprocessingError(Exception):
    """
    Base preprocessing exception.
    """
    pass


class FeatureValidationError(
    PreprocessingError
):
    """
    Raised when feature validation fails.
    """
    pass


class FeatureSchemaError(
    PreprocessingError
):
    """
    Raised when schema integrity fails.
    """
    pass


class FeatureNormalizationError(
    PreprocessingError
):
    """
    Raised when normalization fails.
    """
    pass
