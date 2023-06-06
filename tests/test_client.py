"""Test for pyesa.client module."""
import pytest
from pyesa import client


@pytest.mark.parametrize(
    "api_host, api_key, debug, expected_client",
    [
        (
            "test.example.com",
            "test-key",
            False,
            client.EsaClient("test.example.com", "test-key", False),
        ),
        (
            "test.example.com",
            "test-key",
            True,
            client.EsaClient("test.example.com", "test-key", True),
        ),
        ("", "test-key", False, client.EsaClient("", "test-key", False)),
        (
            "test.example.com",
            "",
            False,
            client.EsaClient("test.example.com", "", False),
        ),
    ],
)
def test_initialize_esa_client(
    api_host: str,
    api_key: str,
    debug: bool,
    expected_client: client.EsaClient,
):
    """Test initialize esa client."""
    esa_client = client.EsaClient(api_host=api_host, api_key=api_key, debug=debug)
    assert esa_client.api_host == expected_client.api_host
    assert esa_client.api_key == expected_client.api_key
    assert esa_client.debug == expected_client.debug
