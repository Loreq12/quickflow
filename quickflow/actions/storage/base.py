from abc import abstractmethod, ABC
from pathlib import Path


class BaseStorageStrategy(ABC):

    # @abstractmethod
    # def auth(self):
    #     raise NotImplementedError

    @abstractmethod
    def list(self, path: Path):
        raise NotImplementedError

    @abstractmethod
    def upload(self):
        raise NotImplementedError

    @abstractmethod
    def download(self):
        raise NotImplementedError
