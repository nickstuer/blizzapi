from .classicClient import ClassicClient


class ClassicEraClient(ClassicClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.namespace_template = "{namespace}-classic1x-{region}"
