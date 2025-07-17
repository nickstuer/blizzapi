from unittest.mock import patch

from blizzapi.clients.wow.classic_client import ClassicClient
from blizzapi.clients.wow.classic_era_client import ClassicEraClient
from blizzapi.clients.wow.retail_client import RetailClient


def mock_get(uri):
    return uri


@patch("blizzapi.clients.wow.classic_client.ClassicClient.get", lambda _, x: mock_get(x))
def test_classic():
    client = ClassicClient("client_id", "client_secret")
    result = client.character_profile("doomhowl", "thetusk")
    assert (
        result
        == "https://us.api.blizzard.com/profile/wow/character/doomhowl/thetusk?namespace=profile-classic-us&locale=en_US"
    )


@patch("blizzapi.clients.wow.classic_era_client.ClassicEraClient.get", lambda _, x: mock_get(x))
def test_classic_era():
    client = ClassicEraClient("client_id", "client_secret")
    result = client.character_profile("doomhowl", "thetusk")
    assert (
        result
        == "https://us.api.blizzard.com/profile/wow/character/doomhowl/thetusk?namespace=profile-classic1x-us&locale=en_US"
    )


@patch("blizzapi.clients.wow.retail_client.RetailClient.get", lambda _, x: mock_get(x))
def test_retail():
    client = RetailClient("client_id", "client_secret")
    result = client.character_profile_summary("doomhowl", "thetusk")
    assert (
        result == "https://us.api.blizzard.com/profile/wow/character/doomhowl/thetusk?namespace=profile-us&locale=en_US"
    )


@patch("blizzapi.clients.wow.retail_client.RetailClient.get", lambda _, x: mock_get(x))
def test_retail_with_fields():
    client = RetailClient("client_id", "client_secret")
    result = client.character_profile_summary("doomhowl", "thetusk", fields={"achievements": "progression"})
    assert (
        result
        == "https://us.api.blizzard.com/profile/wow/character/doomhowl/thetusk?namespace=profile-us&locale=en_US&achievements=progression"
    )
