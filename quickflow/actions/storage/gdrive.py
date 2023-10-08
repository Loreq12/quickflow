from abc import ABC

from quickflow.actions.storage.base import BaseStorageStrategy


class GDriveStorageStrategy(BaseStorageStrategy, ABC):

    def upload(self):
        ...

    def download(self):
        ...
