import requests


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r: requests.Request):
        r.headers["authorization"] = "Bearer " + self.token
        return r


def get_args_from_func(fn, args, kwargs) -> dict:
    args_names = fn.__code__.co_varnames[: fn.__code__.co_argcount]
    variables = {**dict(zip(args_names, args)), **kwargs}
    return variables


def get_clean_args(variables: dict) -> dict:
    clean = {}
    for k, v in variables.items():
        if isinstance(v, (str, int, float, bool)):
            clean[k] = v
    return clean


def parse_uri(command_uri: str, variables: dict) -> str:
    uri = command_uri
    for k, v in variables.items():
        uri = uri.replace("{" + str(k) + "}", str(v))
    return uri


def append_param(uri: str, param: str) -> str:
    if "?" in uri:
        return uri + "&" + param
    else:
        return uri + "?" + param
