from abc import abstractmethod, ABC


class BaseInvoiceStrategy(ABC):

    @abstractmethod
    def list_invoices(self):
        raise NotImplementedError

    @abstractmethod
    def create_invoice(self, invoice_data):
        raise NotImplementedError

    @abstractmethod
    def download_invoice(self, invoice_id: str):
        raise NotImplementedError
