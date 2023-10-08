from pathlib import Path

from quickflow.actions.mail.gmail import GMailStrategy
from quickflow.actions.storage.gdrive import GDriveStorageStrategy


def run():
    # storage = GDriveStorageStrategy()
    # path = Path("/")
    # storage.list(path)
    mail = GMailStrategy()
    mail.get_mail()


if __name__ == "__main__":
    run()
