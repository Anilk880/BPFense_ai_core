from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = BASE_DIR.parent

EXPORTS_DIR = PROJECT_ROOT / "exports"

TF_MODEL_PATH = (
    EXPORTS_DIR
    / "tensorflow"
    / "bpfense_saved_model"
)

SKLEARN_MODEL_PATH = (
    EXPORTS_DIR
    / "sklearn"
    / "model.pkl"
)

AUTOENCODER_MODEL_PATH = (
    EXPORTS_DIR
    / "autoencoder"
    / "behavioral_autoencoder"
)

SEQUENCE_MODEL_PATH = (
    EXPORTS_DIR
    / "sequence"
    / "behavioral_lstm_model"
)
