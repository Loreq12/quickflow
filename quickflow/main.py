import contextlib
from typing import Callable

from fastapi import Depends, FastAPI

from quickflow.config import Settings
from quickflow.db import get_async_db
from quickflow.external_actions.chain.invoice import (InvoiceHandler)
from quickflow.external_actions.chain.models import InvoiceAction
from quickflow.external_actions.strategy.base import AbstractServiceStrategy
from quickflow.external_actions.strategy.invoice.base import \
    BaseInvoiceStrategy
from quickflow.external_actions.strategy.invoice.wfirma import \
    WFirmaInvoiceStrategy
from quickflow.logs.middleware import LogMiddleware
from quickflow.models import User
from quickflow.tasks.test import test_task


def run():
    # storage = GDriveStorageStrategy()
    # path = Path("/")
    # storage.list(path)
    # mail = GMailStrategy()
    # mail.get_mail()
    invoices = WFirmaInvoiceStrategy()
    invoices.create_invoice()


@contextlib.asynccontextmanager
async def lifespan(app):
    print("Run on startup!")

    yield

    print("Run on shutdown!")


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.add_middleware(LogMiddleware)

    @app.get("/ok")
    async def hello_ok(db = Depends(get_async_db)):
        await User.get_by_email(db, "ceziu1997@gmIL.COM")
        test_task.delay(4, 4)
        return "Hello World"

    @app.get("/exception")
    async def hello_exc():
        msg = "Coś jebło"
        raise ValueError(msg)

    return app


if __name__ == "__main__":
    settings = Settings()

    handler = InvoiceHandler(service_name="WFirma")
    handler.execute_next(InvoiceAction.CREATE)

    # data: BaseInvoiceStrategy = AbstractServiceStrategy.get_service_by_name("WFirma")()
    # mapper: dict[InvoiceAction, Callable] = data.get_action_to_function_mapper()
    # run()
#     uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None, reload=True)
