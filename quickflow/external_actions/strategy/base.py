from abc import ABC, abstractmethod
from enum import Enum
from functools import lru_cache
from typing import Callable, Generic, Self, Type, TypeVar

from quickflow.consts import AvailableModules
from quickflow.logs.logger import logger


class AbstractAction(Enum):
    ...


T = TypeVar("T", bound=AbstractAction)


class AbstractServiceStrategy(ABC, Generic[T]):

    service_name: str = "Dummy"
    module_name: AvailableModules = AvailableModules.DUMMY
    actions: Type[AbstractAction] = AbstractAction

    def get_action_to_function_mapper(self) -> dict[T, Callable]:
        raise NotImplementedError

    @classmethod
    @lru_cache
    def get_all_services(cls) -> dict[str, Type]:
        result: dict[str, Type[AbstractServiceStrategy[T]]] = {}

        for service_abc in cls.__subclasses__():
            result |= {
                k.service_name: k for k in service_abc.__subclasses__()
            }

        return result

    @classmethod
    def get_service_by_name(cls, service_name: str) -> Type[Self]:
        svcs = cls.get_all_services()
        result: Type[Self]
        try:
            result = svcs[service_name]
        except KeyError:
            msg = f"{service_name=} was not found. Probably not registered?"
            logger.error(msg)
            raise

        # TODO: Return Dummy Strategy of given type
        return result
