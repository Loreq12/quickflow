import logging

import uvicorn

from fastapi import FastAPI

from quickflow.actions.invoice.wfirma import WFirmaInvoiceStrategy
from quickflow.actions.mail.gmail import GMailStrategy
from quickflow.logs.middleware import LogMiddleware
from quickflow.logs import base_logger


def run():
    # storage = GDriveStorageStrategy()
    # path = Path("/")
    # storage.list(path)
    # mail = GMailStrategy()
    # mail.get_mail()
    invoices = WFirmaInvoiceStrategy()
    invoices.create_invoice()


app = FastAPI()
app.add_middleware(LogMiddleware)


@app.get("/ok")
async def hello_ok():
    return "Hello World"


@app.get("/exception")
async def hello_exc():
    msg = "Coś jebło"
    raise ValueError(msg)


if __name__ == "__main__":
    run()
#     uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None, reload=True)
