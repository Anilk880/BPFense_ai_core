from dataclasses import dataclass

from typing import Dict
from typing import Any


@dataclass
class PredictionRequest:

    features: Dict[str, Any]


@dataclass
class PredictionResponse:

    label: str

    severity: str

    score: float

    backend: str
