import os

from fastapi import File
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pydantic import EmailStr

from quickflow.external_actions.strategy.mail.base import BaseMailStrategy, EmailSchema


class GMailStrategy(BaseMailStrategy):

    service_name = "Google Mail"

    def auth(self) -> dict:
        ...

    def get_mails(self, **kwargs) -> list:
        ...
        # creds = None
        # SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
        # # The file token.json stores the user's access and refresh tokens, and is
        # # created automatically when the authorization flow completes for the first
        # # time.
        # if os.path.exists("token.json"):
        #     creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # # If there are no (valid) credentials available, let the user log in.
        # if not creds or not creds.valid:
        #     if creds and creds.expired and creds.refresh_token:
        #         creds.refresh(Request())
        #     else:
        #         flow = InstalledAppFlow.from_client_secrets_file(
        #             "credentials.json", SCOPES
        #         )
        #         creds = flow.run_local_server(port=0)
        #     # Save the credentials for the next run
        #     with open("token.json", "w") as token:
        #         token.write(creds.to_json())
        #
        # try:
        #     # Call the Gmail API
        #     service = build("gmail", "v1", credentials=creds)
        #     results = service.users().labels().list(userId="me").execute()
        #     labels = results.get("labels", [])
        #
        #     if not labels:
        #         print("No labels found.")
        #         return
        #     print("Labels:")
        #     for label in labels:
        #         print(label["name"])
        #
        # except HttpError as error:
        #     # TODO(developer) - Handle errors from gmail API.
        #     print(f"An error occurred: {error}")

    def get_last_mail(self, from_address: EmailStr) -> EmailSchema | None:
        creds = self.auth()
        emails = self.get_mails(from_address=from_address)
        if not emails:
            return None

        email: dict = emails[0]
        return EmailSchema(
            content=email["content"],
            attachments={att["name"]: att["base64"] for att in email["attachment"]}
        )

    def send_mail(self, attachments: list):
        ...
