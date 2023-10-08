import uvicorn

from fastapi import FastAPI

from quickflow.actions.mail.gmail import GMailStrategy
from quickflow.logs.logger import logger
from quickflow.logs.middleware import LogMiddleware


def run():
    # storage = GDriveStorageStrategy()
    # path = Path("/")
    # storage.list(path)
    mail = GMailStrategy()
    mail.get_mail()


app = FastAPI()
app.add_middleware(LogMiddleware)


@app.get("/ok")
async def hello():
    return "Hello World"

@app.get("/exception")
async def hello():
    msg = "Coś jebło"
    raise ValueError(msg)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None, reload=True)
