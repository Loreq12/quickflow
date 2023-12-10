from enum import Enum, StrEnum, auto


class RequestsDataEnum(StrEnum):
    REQUEST_TO_SERVER = "req"
    RESPONSE_FROM_SERVER = "res"
    EXCEPTION = "exc"


class AvailableModules(Enum):
    DUMMY = -1

    INVOICE = auto()
    STORAGE = auto()
    MAIL = auto()
