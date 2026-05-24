from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class PredictionResult:
    backend: str
    label: str
    score: float
    severity: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    raw_output: Optional[Any] = None
