from abc import abstractmethod, ABC

from quickflow.actions.invoice.base import BaseInvoiceStrategy


class WFirmaInvoiceStrategy(BaseInvoiceStrategy, ABC):

    @abstractmethod
    def create_invoice(self, invoice_data):
        ...

    @abstractmethod
    def download_invoice(self, invoice_id: str):
        ...
