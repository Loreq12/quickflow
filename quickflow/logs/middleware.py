import sys

from enum import StrEnum

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from quickflow.logs import base_logger


class RequestsDataEnum(StrEnum):
    REQUEST_TO_SERVER = "req"
    RESPONSE_FROM_SERVER = "res"
    EXCEPTION = "exc"


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        base_logger.info(
            "Got request to server",
            extra={
                RequestsDataEnum.REQUEST_TO_SERVER: {"method": request.method, "url": str(request.url)},
            }
        )

        response = await call_next(request)

        base_logger.info(
            "Request finished",
            extra={
                RequestsDataEnum.RESPONSE_FROM_SERVER: {"status_code": response.status_code},
            },
        )
        return response


class ExceptionLoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
        except Exception:
            base_logger.error(
                "Got unhandled exception",
                extra={
                    RequestsDataEnum.EXCEPTION: sys.exc_info(),
                },
            )
            return JSONResponse({"detail": "Error", "other_stuff": "blah"})
        else:
            return response
