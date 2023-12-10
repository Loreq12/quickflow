from quickflow.external_actions.chain.base import Handler
from quickflow.external_actions.chain.models import StorageAction


class StorageHandler(Handler):

    def _execute(self, request: StorageAction):
        ...
