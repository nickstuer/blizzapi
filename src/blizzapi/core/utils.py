import requests

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r: requests.Request):
        r.headers["authorization"] = "Bearer " + self.token
        return r
    
def get_args_dict(fn, args, kwargs):
    args_names = fn.__code__.co_varnames[:fn.__code__.co_argcount]
    variables = {**dict(zip(args_names, args)), **kwargs}
    keys_to_delete = []
    for k,v in variables.items():
        if not isinstance(v, (str, int, float, bool)):
            keys_to_delete.append(k)
    for k in keys_to_delete:
        del variables[k]
    return variables

def parse_uri(command_uri: str, variables: dict):
    uri = command_uri
    for k,v in variables.items():
        uri = uri.replace('{' + k + '}', v)
    return uri

def append_param(uri: str, param: str):
    if '?' in uri:
        return uri + '&' + param
    else:
        return uri + '?' + param