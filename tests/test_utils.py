import requests

from blizzapi.core.utils import (
    BearerAuth,
    append_param,
    get_args_from_func,
    get_clean_args,
    parse_uri,
)


def test_bearer_auth_adds_header():
    token = "testtoken"
    auth = BearerAuth(token)
    req = requests.Request("GET", "http://example.com")
    prepared = req.prepare()
    # Simulate call
    auth(prepared)
    assert prepared.headers["authorization"] == f"Bearer {token}"


def dummy_func(a, b, c=3):
    pass


def test_get_args_from_func():
    args = (1, 2)
    kwargs = {"c": 4}
    result = get_args_from_func(dummy_func, args, kwargs)
    assert result == {"a": 1, "b": 2, "c": 4}


def test_get_clean_args_filters_types():
    variables = {
        "a": 1,
        "b": "string",
        "c": 3.14,
        "d": True,
        "e": [1, 2, 3],
        "f": {"x": 1},
        "g": None,
    }
    clean = get_clean_args(variables)
    assert clean == {"a": 1, "b": "string", "c": 3.14, "d": True}


def test_parse_uri_replaces_variables():
    command_uri = "/foo/{bar}/baz/{qux}"
    variables = {"bar": 123, "qux": "abc"}
    result = parse_uri(command_uri, variables)
    assert result == "/foo/123/baz/abc"


def test_append_param_with_existing_query():
    uri = "/foo?bar=1"
    param = "baz=2"
    result = append_param(uri, param)
    assert result == "/foo?bar=1&baz=2"


def test_append_param_without_query():
    uri = "/foo"
    param = "bar=1"
    result = append_param(uri, param)
    assert result == "/foo?bar=1"
