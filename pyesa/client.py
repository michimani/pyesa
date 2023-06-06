"""Client for Esa API."""
from dataclasses import dataclass


@dataclass(frozen=True)
class EsaClient:
    """Client for Esa API."""

    api_host: str
    api_key: str
    debug: bool = False
