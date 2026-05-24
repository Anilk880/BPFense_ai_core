class BPFenseError(Exception):
    pass


class ValidationError(BPFenseError):
    pass


class PredictionError(BPFenseError):
    pass


class ModelLoadError(BPFenseError):
    pass
