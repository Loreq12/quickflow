from urllib.parse import urljoin

import requests

from typing import Literal

from quickflow.logs import base_logger
from quickflow.logs.middleware import RequestsDataEnum


class RestAPIClient:
    def __init__(self, host: str, headers: dict):
        self.host = host
        self.headers = headers

    def _get_full_url(self, path: str) -> str:
        return urljoin(self.host, path)

    def make_request(self, path: str, method: Literal["GET", "POST"], json_data: dict):
        base_logger.info(
            f"Sending request to {path}",
            extra={
                RequestsDataEnum.REQUEST_TO_SERVER: {
                    "method": method,
                    "json": json_data,
                }
            },
        )
        response = requests.request(method, path, json=json_data, headers=self.headers)
        parsed_data = self._handle_response(response)

        return parsed_data

    @classmethod
    def _parse_data(cls, response: requests.Response):
        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            data = response.text
            base_logger.error(
                f"Can not decode response data from {response.url}",
                extra={RequestsDataEnum.RESPONSE_FROM_SERVER: data},
            )
            raise  # IDK what for now

        return data

    @classmethod
    def _handle_response(cls, response: requests.Response):
        try:
            data = cls._parse_data(response)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            base_logger.error(
                f"Got request from {response.url}",
                extra={
                    RequestsDataEnum.RESPONSE_FROM_SERVER: {
                        "status": response.status_code,
                        "json": data,
                    }
                },
            )
            raise
        else:
            base_logger.info(
                f"Got request from {response.url}",
                extra={
                    RequestsDataEnum.RESPONSE_FROM_SERVER: {
                        "status": response.status_code,
                        "json": data,
                    }
                },
            )
