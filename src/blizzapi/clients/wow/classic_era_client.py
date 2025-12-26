from blizzapi.core.enums import Language, Region

from .classic_client import ClassicClient


class ClassicEraClient(ClassicClient):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        region: Region = Region.US,
        language: Language = Language.English,
    ):
        super().__init__(client_id, client_secret, region, language)
        self.namespace_template = "{namespace}-classic1x-{region}"
