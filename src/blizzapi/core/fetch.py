from functools import wraps

from blizzapi.core.baseClient import BaseClient
from blizzapi.core.oAuth2Client import OAuth2Client


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

                result = client.get(uri)
                return result

            return wrapped

        return wrapped


dynamic = Fetch("dynamic").fetch
profile = Fetch("profile").fetch
static = Fetch("static").fetch
