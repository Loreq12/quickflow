from quickflow.external_actions.chain.base import Handler
from quickflow.external_actions.chain.models import MailAction
from quickflow.external_actions.strategy.mail.base import BaseMailStrategy


class MailHandler(Handler):

    def _execute(self, action: MailAction):
        strategy: BaseMailStrategy = self._strategy()
        mapped_function = strategy.get_action_to_function_mapper()[action]

        match action:
            case MailAction.GET_FROM_ADDRESS:
                data = mapped_function()
            case MailAction.SEND:
                data = mapped_function()

        return {}
