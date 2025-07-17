from unittest.mock import patch

import pytest

from blizzapi.core.fetch import Fetch, dynamic, profile, static


class DummyClient:
    def build_uri(self, command_uri, namespace_type, func, args, kwargs):
        return f"https://api.test/{namespace_type}/{command_uri}"

    def get(self, uri):
        return {"uri": uri}


class DummyOAuth2Client(DummyClient):
    pass


@patch("blizzapi.core.fetch.OAuth2Client", new=DummyOAuth2Client)
def test_fetch_decorator_calls_build_uri_and_get():
    client = DummyOAuth2Client()
    fetcher = Fetch("dynamic")
    command_uri = "test/endpoint"

    @fetcher.fetch(command_uri)
    def test_func(self, param1):
        pass

    with (
        patch.object(client, "build_uri", wraps=client.build_uri) as mock_build_uri,
        patch.object(client, "get", wraps=client.get) as mock_get,
    ):
        result = test_func(client, "foo")
        mock_build_uri.assert_called_once()
        mock_get.assert_called_once()
        assert result == {"uri": "https://api.test/dynamic/test/endpoint"}


@patch("blizzapi.core.fetch.OAuth2Client", new=DummyOAuth2Client)
def test_dynamic_profile_static_shortcuts():
    client = DummyOAuth2Client()

    @dynamic("foo/bar")
    def dyn_func(self):
        pass

    @profile("baz/qux")
    def prof_func(self):
        pass

    @static("abc/xyz")
    def stat_func(self):
        pass

    assert dyn_func(client) == {"uri": "https://api.test/dynamic/foo/bar"}
    assert prof_func(client) == {"uri": "https://api.test/profile/baz/qux"}
    assert stat_func(client) == {"uri": "https://api.test/static/abc/xyz"}


def test_fetch_decorator_asserts_oauth2client():
    fetcher = Fetch("dynamic")

    @fetcher.fetch("foo/bar")
    def test_func(self):
        pass

    class NotOAuth2Client:
        pass

    with pytest.raises(TypeError):
        test_func(NotOAuth2Client())
