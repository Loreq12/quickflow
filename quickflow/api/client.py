from typing import Literal

import requests


class RestAPIClient:

    # def __init__(self, url: str):
    #     self.ur

    def make_request(self, path: str, method: Literal["GET", "POST"], headers: dict, json_data: dict):
        return requests.request(method, path, json=json_data, headers=headers)
