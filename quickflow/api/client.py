from typing import Literal

import requests


class RestAPIClient:

    def make_request(self, url: str, method: Literal["GET", "POST"], headers: dict, json_data: dict):
        requests.request(method, url, json=json_data, headers=headers)
