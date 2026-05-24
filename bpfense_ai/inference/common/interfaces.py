from abc import ABC, abstractmethod
from .types import PredictionResult


class InferenceBackend(ABC):

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def predict(self, features) -> PredictionResult:
        pass

    @abstractmethod
    def healthy(self) -> bool:
        pass
