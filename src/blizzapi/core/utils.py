from collections.abc import Callable

import requests


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token: str):
        self.token = token

    def __call__(self, r: requests.Request):
        r.headers["authorization"] = "Bearer " + self.token
        return r


def get_args_from_func(fn: Callable, args: tuple, kwargs: dict) -> dict:
    args_names = fn.__code__.co_varnames[: fn.__code__.co_argcount]
    return {**dict(zip(args_names, args, strict=False)), **kwargs}


def get_clean_args(variables: dict) -> dict:
    return {k: v for k, v in variables.items() if isinstance(v, (str, int, float, bool))}


def parse_uri(command_uri: str, variables: dict) -> str:
    uri = command_uri
    for k, v in variables.items():
        uri = uri.replace("{" + str(k) + "}", str(v))
    return uri


def append_param(uri: str, param: str) -> str:
    if "?" in uri:
        return uri + "&" + param
    return uri + "?" + param
