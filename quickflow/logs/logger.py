import json
import logging
from logging import Formatter


class JsonFormatter(Formatter):

    def format(self, record):
        from quickflow.logs.middleware import RequestsDataEnum

        json_record = {"message": record.getMessage()}

        match record.__dict__:
            case {RequestsDataEnum.REQUEST_TO_SERVER: data, **rest}:
                json_record[RequestsDataEnum.REQUEST_TO_SERVER] = data
            case {RequestsDataEnum.RESPONSE_FROM_SERVER: data, **rest}:
                json_record[RequestsDataEnum.RESPONSE_FROM_SERVER] = data
            case {RequestsDataEnum.EXCEPTION: data, **rest}:
                json_record[RequestsDataEnum.EXCEPTION] = self.formatException(data)

        return json.dumps(json_record)


logger = logging.root
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.handlers = [handler]
logger.setLevel(logging.DEBUG)
logging.getLogger("uvicorn.access").disabled = True
