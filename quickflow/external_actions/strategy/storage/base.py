from abc import ABC, abstractmethod
from pathlib import Path
from typing import Callable

from quickflow.consts import AvailableModules
from quickflow.external_actions.chain.models import StorageAction
from quickflow.external_actions.strategy.base import AbstractServiceStrategy


class BaseStorageStrategy(AbstractServiceStrategy, ABC):

    module_name = AvailableModules.STORAGE
    actions = StorageAction

    def get_action_to_function_mapper(self) -> dict[StorageAction, Callable]:
        return {
            StorageAction.DOWNLOAD: self.download,
            StorageAction.LIST: self.list,
            StorageAction.UPLOAD: self.upload,
        }

    @abstractmethod
    def list(self, path: Path):
        raise NotImplementedError

    @abstractmethod
    def upload(self):
        raise NotImplementedError

    @abstractmethod
    def download(self):
        raise NotImplementedError
