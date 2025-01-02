import importlib.metadata
DISTRIBUTION_NAME = "blizzapi"

__version__ = importlib.metadata.version(DISTRIBUTION_NAME)

from .clients.wow.classicEraClient import ClassicEraClient
from .core.enums import Language, Region


print(__version__)