from bpfense_ai import (
    BPFenseClient,
)

from bpfense_ai.testing.replay_loader import (
    load_replay_sample,
)

# =========================================================
# CLIENT
# =========================================================

client = BPFenseClient()

client.load()

# =========================================================
# HELPER
# =========================================================

def assert_behavior(
    replay_path,
    expected="malicious",
    min_score=0.0,
    max_score=1.0,
):

    sample = load_replay_sample(
        replay_path
    )

    result = client.predict(
        sample
    )

    print("\n===================================")
    print(replay_path)
    print("===================================")

    print(result)

    assert result.label == (
        expected
    )

    assert (
        min_score
        <= result.score
        <= max_score
    )

# =========================================================
# BENIGN TERMINAL
# =========================================================

def test_benign_behavior():

    assert_behavior(

        "tests/golden/benign/"
        "normal_terminal_usage.json",

        expected="normal",

        max_score=0.50,
    )

# =========================================================
# REVERSE SHELL
# =========================================================

def test_reverse_shell_detection():

    assert_behavior(

        "tests/golden/malicious/"
        "reverse_shell.json",

        expected="malicious",

        min_score=0.70,
    )

# =========================================================
# DNS BEACONING
# =========================================================

def test_dns_beaconing_detection():

    assert_behavior(

        "tests/golden/malicious/"
        "dns_beaconing.json",

        expected="malicious",

        min_score=0.60,
    )

# =========================================================
# PORT SCAN
# =========================================================

def test_port_scan_detection():

    assert_behavior(

        "tests/golden/malicious/"
        "port_scan.json",

        expected="malicious",

        min_score=0.70,
    )

# =========================================================
# DATA EXFILTRATION
# =========================================================

def test_data_exfiltration_detection():

    assert_behavior(

        "tests/golden/malicious/"
        "data_exfiltration.json",

        expected="malicious",

        min_score=0.80,
    )

# =========================================================
# CRYPTO MINER
# =========================================================

def test_crypto_miner_detection():

    assert_behavior(

        "tests/golden/malicious/"
        "crypto_miner.json",

        expected="malicious",

        min_score=0.75,
    )

# =========================================================
# LATERAL MOVEMENT
# =========================================================

def test_lateral_movement_detection():

    assert_behavior(

        "tests/golden/malicious/"
        "lateral_movement.json",

        expected="malicious",

        min_score=0.75,
    )

# =========================================================
# PRIVILEGE ESCALATION
# =========================================================

def test_privilege_escalation_detection():

    assert_behavior(

        "tests/golden/malicious/"
        "privilege_escalation.json",

        expected="malicious",

        min_score=0.80,
    )

# =========================================================
# C2 BEACONING
# =========================================================

def test_c2_beaconing_detection():

    assert_behavior(

        "tests/golden/malicious/"
        "c2_beaconing.json",

        expected="malicious",

        min_score=0.80,
    )
