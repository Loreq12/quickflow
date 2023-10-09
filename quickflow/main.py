import contextlib
import logging

import uvicorn
from celery import Celery

from fastapi import Depends, FastAPI

from quickflow.actions.invoice.wfirma import WFirmaInvoiceStrategy
from quickflow.actions.mail.gmail import GMailStrategy
from quickflow.config import Settings, get_settings
from quickflow.db import get_async_db
from quickflow.logs.middleware import LogMiddleware
from quickflow.logs import base_logger
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
    run()
#     uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None, reload=True)
