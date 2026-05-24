from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

EXPORTS_DIR = (
    BASE_DIR / "exports"
)

# =========================================
# TensorFlow
# =========================================

TF_MODEL_PATH = (
    EXPORTS_DIR
    / "tensorflow"
    / "bpfense_saved_model"
)

# =========================================
# Sklearn
# =========================================

SKLEARN_MODEL_PATH = (
    EXPORTS_DIR
    / "sklearn"
    / "model.pkl"
)

# =========================================
# Autoencoder
# =========================================

AUTOENCODER_MODEL_PATH = (
    EXPORTS_DIR
    / "autoencoder"
    / "behavioral_autoencoder"
)

# =========================================
# Sequence
# =========================================

SEQUENCE_MODEL_PATH = (
    EXPORTS_DIR
    / "sequence"
    / "behavioral_lstm_model"
)
