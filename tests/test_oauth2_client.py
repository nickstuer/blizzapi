from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

import pytest

from blizzapi.core.oauth2_client import OAuth2Client


@pytest.fixture
def oauth2_client():
    return OAuth2Client(
        client_id="test_id",
        client_secret="test_secret",
        token_uri="https://example.com/token",
        token_expiration_grace_period=1,
    )


@patch("blizzapi.core.oauth2_client.BearerAuth")
@patch.object(OAuth2Client, "refresh_token")
def test_get_calls_refresh_and_returns_json(mock_refresh, mock_bearer, oauth2_client):
    mock_response = MagicMock()
    mock_response.json.return_value = {"foo": "bar"}
    oauth2_client.s.get = MagicMock(return_value=mock_response)
    oauth2_client.token = {
        "access_token": "abc",
        "expires_at": datetime.now(timezone.utc).timestamp() + 100,
    }
    result = oauth2_client.get("https://api.example.com/data")
    mock_refresh.assert_called_once()
    oauth2_client.s.get.assert_called_once()
    assert result == {"foo": "bar"}


@patch("blizzapi.core.oauth2_client.OAuth2Session")
@patch("blizzapi.core.oauth2_client.BackendApplicationClient")
def test_get_new_token_sets_token(mock_backend_client, mock_oauth2session, oauth2_client):
    mock_oauth = MagicMock()
    mock_oauth.fetch_token.return_value = {
        "access_token": "abc",
        "expires_at": 1234567890,
    }
    mock_oauth2session.return_value = mock_oauth
    oauth2_client.get_new_token()
    assert oauth2_client.token == {"access_token": "abc", "expires_at": 1234567890}
    mock_oauth.fetch_token.assert_called_once()


def test_token_expiring_soon_true(oauth2_client):
    now = datetime.now(timezone.utc)
    oauth2_client.token = {"expires_at": (now + timedelta(seconds=30)).timestamp()}
    oauth2_client.token_expiration_grace_period = 1  # 1 minute
    assert oauth2_client.token_expiring_soon() is True


def test_token_expiring_soon_false(oauth2_client):
    now = datetime.now(timezone.utc)
    oauth2_client.token = {"expires_at": (now + timedelta(minutes=10)).timestamp()}
    oauth2_client.token_expiration_grace_period = 1  # 1 minute
    assert oauth2_client.token_expiring_soon() is False


@patch.object(OAuth2Client, "get_new_token")
def test_refresh_token_none_triggers_get_new_token(mock_get_new_token, oauth2_client):
    oauth2_client.token = None
    oauth2_client.refresh_token()
    mock_get_new_token.assert_called_once()


@patch.object(OAuth2Client, "get_new_token")
@patch.object(OAuth2Client, "token_expiring_soon", return_value=True)
def test_refresh_token_expiring_triggers_get_new_token(mock_expiring, mock_get_new_token, oauth2_client):
    oauth2_client.token = {"access_token": "abc", "expires_at": 1234567890}
    oauth2_client.refresh_token()
    mock_get_new_token.assert_called_once()


@patch.object(OAuth2Client, "get_new_token")
@patch.object(OAuth2Client, "token_expiring_soon", return_value=False)
def test_refresh_token_not_expiring_does_not_trigger_get_new_token(mock_expiring, mock_get_new_token, oauth2_client):
    oauth2_client.token = {"access_token": "abc", "expires_at": 1234567890}
    oauth2_client.refresh_token()
    mock_get_new_token.assert_not_called()
