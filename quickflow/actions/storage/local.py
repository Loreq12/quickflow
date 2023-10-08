from pathlib import Path

from quickflow.actions.storage.base import BaseStorageStrategy


class LocalStorageStrategy(BaseStorageStrategy):
    def list(self, path: Path):
        ...

    def upload(self):
        ...

    def download(self):
        ...
