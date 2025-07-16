from unittest.mock import patch

import pytest

from blizzapi.clients.wow.classicClient import ClassicClient


def mock_get(uri):
    return uri


@pytest.fixture
def client():
    return ClassicClient("client_id", "client_secret")


@patch("blizzapi.clients.wow.classicClient.ClassicClient.get", lambda _, x: mock_get(x))
def test_character_profile_calls_profile_decorator(client):
    result = client.character_profile("doomhowl", "thetusk")
    assert (
        result
        == "https://us.api.blizzard.com/profile/wow/character/doomhowl/thetusk?namespace=profile-classic-us&locale=en_US"
    )
