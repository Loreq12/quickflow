from quickflow.consts import AvailableModules
from quickflow.external_actions.strategy.invoice import WFirmaInvoiceStrategy, BaseInvoiceStrategy
from quickflow.external_actions.strategy.mail import GMailStrategy, BaseMailStrategy
from quickflow.external_actions.strategy.storage import GDriveStorageStrategy, BaseStorageStrategy

BASE_STRATEGIES = [
    BaseInvoiceStrategy,
    BaseMailStrategy,
    BaseStorageStrategy,
]

STORAGE_STRATEGIES = [
    GDriveStorageStrategy,
]

MAIL_STRATEGIES = [
    GMailStrategy,
]

INVOICE_STRATEGIES = [
    WFirmaInvoiceStrategy,
]

AVAILABLE_MODULES = {
    AvailableModules.INVOICE: {
        s.service_name: s for s in INVOICE_STRATEGIES
    },
    AvailableModules.MAIL: {
        s.service_name: s for s in MAIL_STRATEGIES
    },
    AvailableModules.STORAGE: {
        s.service_name: s for s in STORAGE_STRATEGIES
    },
}
