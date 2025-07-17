from .classic_client import ClassicClient


class ClassicEraClient(ClassicClient):
    def __init__(self, *args: tuple, **kwargs: dict):
        super().__init__(*args, **kwargs)
        self.namespace_template = "{namespace}-classic1x-{region}"
