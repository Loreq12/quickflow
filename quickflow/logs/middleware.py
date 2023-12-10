import sys

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from quickflow.consts import RequestsDataEnum
from quickflow.logs import base_logger


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        base_logger.info(
            "Got request to server",
            extra={
                RequestsDataEnum.REQUEST_TO_SERVER: {
                    "method": request.method,
                    "url": str(request.url),
                },
            },
        )

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

        base_logger.info(
            "Request finished",
            extra={
                RequestsDataEnum.RESPONSE_FROM_SERVER: {
                    "status_code": response.status_code
                },
            },
        )
        return response
