from abc import abstractmethod


class BaseStorageStrategy:

    @abstractmethod
    def auth(self):
        raise NotImplementedError

    @abstractmethod
    def upload(self):
        raise NotImplementedError

    @abstractmethod
    def download(self):
        raise NotImplementedError
