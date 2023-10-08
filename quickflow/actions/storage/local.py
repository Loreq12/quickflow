from abc import ABC

from quickflow.actions.storage.base import BaseStorageStrategy


class LocalStorageStrategy(BaseStorageStrategy, ABC):

    def upload(self):
        ...

    def download(self):
        ...
