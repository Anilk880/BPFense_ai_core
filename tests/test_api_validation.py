import pytest

from bpfense_ai import (
    BPFenseClient,
)

from bpfense_ai.api.exceptions import (
    ValidationError,
)


def test_invalid_none_features():

    client = BPFenseClient()

    with pytest.raises(
        ValidationError
    ):

        client.predict(None)


def test_invalid_non_dict_features():

    client = BPFenseClient()

    with pytest.raises(
        ValidationError
    ):

        client.predict("invalid")


def test_empty_features():

    client = BPFenseClient()

    with pytest.raises(
        ValidationError
    ):

        client.predict({})
