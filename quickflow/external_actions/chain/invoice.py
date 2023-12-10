from quickflow.external_actions.chain.base import Handler
from quickflow.external_actions.chain.models import InvoiceAction
from quickflow.external_actions.strategy.invoice.base import BaseInvoiceStrategy


class InvoiceHandler(Handler):

    def _execute(self, action: InvoiceAction) -> dict:
        strategy: BaseInvoiceStrategy = self._strategy()
        mapped_function = strategy.get_action_to_function_mapper()[action]

        match action:
            case InvoiceAction.LIST | InvoiceAction.CREATE:
                data = mapped_function()
            case InvoiceAction.DOWNLOAD:
                data = mapped_function()

        return {}
        # data = InvoiceResultData()
        # return ActionResult(data=data)
