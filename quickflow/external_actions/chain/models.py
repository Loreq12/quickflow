from enum import auto

from quickflow.external_actions.strategy.base import AbstractAction


class InvoiceAction(AbstractAction):
    LIST = auto()
    CREATE = auto()
    DOWNLOAD = auto()


class MailAction(AbstractAction):
    GET_FROM_ADDRESS = auto()
    SEND = auto()


class StorageAction(AbstractAction):
    LIST = auto()
    UPLOAD = auto()
    DOWNLOAD = auto()
