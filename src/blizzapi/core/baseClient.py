from blizzapi.core.oAuth2Client import OAuth2Client
from blizzapi.core.enums import Region, Language
from blizzapi.core.constants import TOKEN_AUTH_URI, API_BASE_URI
from blizzapi.core.utils import (
    get_args_from_func,
    parse_uri,
    append_param,
    get_clean_args,
)


class BaseClient(OAuth2Client):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        region: Region = Region.US,
        language: Language = Language.English,
    ):
        self.region = region.value
        self.language = language.value
        self.namespace_template = ""
        token_auth_uri = TOKEN_AUTH_URI[self.region]
        super().__init__(client_id, client_secret, token_auth_uri)

    def build_uri(
        self, command_uri: str, namespace_type: str, func, args, kwargs
    ) -> str:
        all_args = get_args_from_func(func, args, kwargs)
        args = get_clean_args(all_args)
        command_uri = parse_uri(command_uri, args)

        namespace = "namespace=" + self.namespace_template
        namespace = namespace.replace("{region}", self.region)
        namespace = namespace.replace("{namespace}", namespace_type)

        api_uri = API_BASE_URI[self.region] + command_uri
        uri = append_param(api_uri, namespace)
        uri = append_param(uri, f"locale={self.language}")

        if "fields" in all_args:
            for k, v in all_args["fields"].items():
                uri = append_param(uri, f"{k}={v}")

        return uri
