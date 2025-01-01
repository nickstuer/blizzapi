from functools import wraps
from blizzapi.core.constants import API_BASE_URI, TOKEN_AUTH_URI
from blizzapi.core.enums import Region, Language
from blizzapi.core.utils import get_args_dict, parse_uri, append_param
from blizzapi.core.oAuth2Client import OAuth2Client

class GoFetch():
    def __init__(self, namespace_type):
        self.namespace_type = namespace_type

    def _build_uri(self, command_uri:str, func, args, kwargs):
        parsed_args = get_args_dict(func, args, kwargs)
        command_uri = parse_uri(command_uri, parsed_args)
        client = args[0]

        namespace = "namespace=" + client.namespace_template
        namespace = namespace.replace('{region}', client.region)
        namespace = namespace.replace('{namespace}', self.namespace_type)

        uri = API_BASE_URI[client.region] + command_uri 
        uri = append_param(uri, namespace)
        uri = append_param(uri, f"locale={client.language}")

        return uri

    def fetch(self, command_uri):
        def wrapped(func):
            @wraps(func)
            def wrapped(*args, **kwargs):
                assert(isinstance(args[0], OAuth2Client))
                client:OAuth2Client = args[0]
                uri = self._build_uri(command_uri, func, args, kwargs)
                return client.get(uri)
            return wrapped
        return wrapped

dynamic = GoFetch('dynamic').fetch
profile = GoFetch('profile').fetch
static = GoFetch('static').fetch