from abc import ABC, abstractmethod
from enum import Enum
from typing import Generic, Self, Type, TypeVar

from quickflow.external_actions.strategy.base import AbstractAction, AbstractServiceStrategy


T = TypeVar("T", bound=AbstractAction)


class Handler(ABC, Generic[T]):
    _next_handler: Self | None = None

    def __init__(self, service_name: str):
        self._strategy: Type = AbstractServiceStrategy.get_service_by_name(service_name)

    def set_next(self, handler: Self) -> Self:
        self._next_handler = handler

        return handler

    @abstractmethod
    def _execute(self, action: T) -> dict:
        ...

    def execute_next(self, action: T):
        result = self._execute(action=action)

        if self._next_handler:
            return self._next_handler.execute_next(action=action)


def build_chain() -> Handler:
    all_handlers: list[Handler] = []  # [Handler(), Handler(), Handler(), Handler()]

    for idx, handler in enumerate(all_handlers):
        if idx + 1 == len(all_handlers):
            break

        handler.set_next(all_handlers[idx + 1])

    return all_handlers[0]
