import json
import os

import requests

from quickflow.actions.invoice.base import BaseInvoiceStrategy


class WFirmaInvoiceStrategy(BaseInvoiceStrategy):
    def list_invoices(self):
        if os.path.exists("credentials_wfirma.json"):
            with open("credentials_wfirma.json") as credentials_file:
                creds = json.load(credentials_file)
        else:
            raise ValueError("Credentials file were not found")

        headers = {
            "accessKey": creds["access_key"],
            "secretKey": creds["secret_key"],
            "appKey": creds["app_key"],
        }
        data = requests.request(
            "GET",
            "https://api2.wfirma.pl/invoices/find?outputFormat=json&inputFormat=json",
            headers=headers,
        )
        print(data)

    def create_invoice(self):
        if os.path.exists("credentials_wfirma.json"):
            with open("credentials_wfirma.json") as credentials_file:
                creds = json.load(credentials_file)
        else:
            raise ValueError("Credentials file were not found")

        headers = {
            "accessKey": creds["access_key"],
            "secretKey": creds["secret_key"],
            "appKey": creds["app_key"],
        }
        data = requests.request(
            "POST",
            "https://api2.wfirma.pl/invoices/add?outputFormat=json&inputFormat=json",
            headers=headers,
        )
        print(data)

    def download_invoice(self, invoice_id: str):
        ...
