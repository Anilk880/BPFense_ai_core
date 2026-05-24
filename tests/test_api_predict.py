from bpfense_ai import (
    BPFenseClient,
)


def test_model_load():

    client = BPFenseClient()

    client.load()

    result = client.health()

    assert result["healthy"] is True


def test_prediction():

    client = BPFenseClient()

    result = client.predict({

        "exec_count": 5,

        "shell_exec_count": 1,

        "net_count": 2,

        "dns_requests": 1,

        "external_connections": 0,
    })

    assert result.label in [
        "normal",
        "malicious",
    ]

    assert isinstance(
        result.score,
        float,
    )

    assert isinstance(
        result.backend,
        str,
    )
