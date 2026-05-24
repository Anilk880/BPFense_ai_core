import hashlib

from bpfense_ai.inference.common.feature_schema import (
    FEATURE_COLUMNS,
)

# =========================================================
# SCHEMA HASH
# =========================================================

def schema_hash() -> str:

    joined = "|".join(
        FEATURE_COLUMNS
    )

    return hashlib.sha256(

        joined.encode()

    ).hexdigest()
