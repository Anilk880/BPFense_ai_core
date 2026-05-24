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
# PRINT RESULT
# =========================================================

def print_result(
    name,
    result,
):

    print("\n===================================")
    print(f"Behavior : {name}")
    print("===================================")

    print(f"Label      : {result.label}")
    print(f"Severity   : {result.severity}")
    print(f"Score      : {result.score:.6f}")
    print(f"Confidence : {result.confidence:.6f}")
    print(f"Backend    : {result.backend}")

# =========================================================
# ASSERT SCORE
# =========================================================

def assert_score(
    replay_path,
    min_score,
    expected_label,
):

    sample = load_replay_sample(
        replay_path
    )

    result = client.predict(
        sample
    )

    print_result(
        replay_path,
        result,
    )

    assert result.label == (
        expected_label
    )

    assert (
        result.score >= min_score
    )

# =========================================================
# BENIGN TEST
# =========================================================

def test_normal_terminal_usage():

    sample = load_replay_sample(

        "tests/golden/benign/"
        "normal_terminal_usage.json"
    )

    result = client.predict(
        sample
    )

    print_result(
        "normal_terminal_usage",
        result,
    )

    assert (
        result.score < 0.50
    )

# =========================================================
# REVERSE SHELL
# =========================================================

def test_reverse_shell_behavior():

    assert_score(

        "tests/golden/malicious/"
        "reverse_shell.json",

        min_score=0.70,

        expected_label="malicious",
    )

# =========================================================
# DNS BEACONING
# =========================================================

def test_dns_beaconing_behavior():

    assert_score(

        "tests/golden/malicious/"
        "dns_beaconing.json",

        min_score=0.60,

        expected_label="malicious",
    )

# =========================================================
# PORT SCAN
# =========================================================

def test_port_scan_behavior():

    assert_score(

        "tests/golden/malicious/"
        "port_scan.json",

        min_score=0.70,

        expected_label="malicious",
    )

# =========================================================
# DATA EXFILTRATION
# =========================================================

def test_data_exfiltration_behavior():

    assert_score(

        "tests/golden/malicious/"
        "data_exfiltration.json",

        min_score=0.80,

        expected_label="malicious",
    )

# =========================================================
# CRYPTO MINER
# =========================================================

def test_crypto_miner_behavior():

    assert_score(

        "tests/golden/malicious/"
        "crypto_miner.json",

        min_score=0.75,

        expected_label="malicious",
    )
