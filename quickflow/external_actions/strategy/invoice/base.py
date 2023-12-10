from abc import ABC, abstractmethod
from typing import Callable

from quickflow.consts import AvailableModules
from quickflow.external_actions.chain.models import InvoiceAction
from quickflow.external_actions.strategy.base import AbstractServiceStrategy


class BaseInvoiceStrategy(AbstractServiceStrategy, ABC):

    module_name: AvailableModules = AvailableModules.INVOICE
    actions = InvoiceAction

    def get_action_to_function_mapper(self) -> dict[InvoiceAction, Callable]:
        return {
            InvoiceAction.DOWNLOAD: self.download_invoice,
            InvoiceAction.LIST: self.list_invoices,
            InvoiceAction.CREATE: self.create_invoice,
        }

    @abstractmethod
    def list_invoices(self):
        raise NotImplementedError

    @abstractmethod
    def create_invoice(self):
        raise NotImplementedError

    @abstractmethod
    def download_invoice(self, invoice_id: str):
        raise NotImplementedError
