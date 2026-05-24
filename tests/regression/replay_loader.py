import json
from pathlib import Path

# =========================================================
# LOAD REPLAY SAMPLE
# =========================================================

def load_replay_sample(path):

    path = Path(path)

    with open(path, "r") as f:

        return json.load(f)
