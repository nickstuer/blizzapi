from functools import wraps
from blizzapi.core.constants import API_BASE_URI, TOKEN_AUTH_URI
from blizzapi.core.enums import Region, Language
from blizzapi.core.utils import get_args_from_func, parse_uri, append_param
from blizzapi.core.oAuth2Client import OAuth2Client
from blizzapi.core.baseClient import BaseClient


class Fetch:
    def __init__(self, namespace_type):
        self.namespace_type = namespace_type

    def fetch(self, command_uri):
        def wrapped(func):
            @wraps(func)
            def wrapped(*args, **kwargs):
                assert isinstance(args[0], OAuth2Client)
                client: BaseClient = args[0]
                uri = client.build_uri(
                    command_uri, self.namespace_type, func, args, kwargs
                )
                return client.get(uri)

            return wrapped

        return wrapped


dynamic = Fetch("dynamic").fetch
profile = Fetch("profile").fetch
static = Fetch("static").fetch
