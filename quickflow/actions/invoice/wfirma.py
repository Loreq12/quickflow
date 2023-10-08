from quickflow.actions.invoice.base import BaseInvoiceStrategy


class WFirmaInvoiceStrategy(BaseInvoiceStrategy):

    def list_invoices(self):
        ...

    def create_invoice(self, invoice_data):
        ...

    def download_invoice(self, invoice_id: str):
        ...
