from bpfense_ai import (
    BPFenseClient,
)


def test_health():

    client = BPFenseClient()

    result = client.health()

    assert result["healthy"] is False
