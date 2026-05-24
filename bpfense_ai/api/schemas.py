from dataclasses import dataclass

from typing import Dict
from typing import Any

# =========================================================
# REQUEST
# =========================================================

@dataclass
class PredictionRequest:

    features: Dict[str, Any]

# =========================================================
# RESPONSE
# =========================================================

@dataclass
class PredictionResponse:

    label: str

    severity: str

    score: float

    confidence: float

    backend: str
