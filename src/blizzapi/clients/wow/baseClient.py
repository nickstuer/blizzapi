from blizzapi.core.oAuth2Client import OAuth2Client
from blizzapi.core.enums import Region, Language
from blizzapi.core.constants import TOKEN_AUTH_URI

class BaseClient(OAuth2Client):
    def __init__(self, client_id:str, client_secret:str, region:Region=Region.US, language:Language=Language.English):
        self.region = region.value
        self.language = language.value
        self.namespace_template = ""
        token_auth_uri = TOKEN_AUTH_URI[self.region]
        super().__init__(client_id, client_secret, token_auth_uri)