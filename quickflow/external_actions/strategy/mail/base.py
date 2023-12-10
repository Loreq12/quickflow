from abc import ABC, abstractmethod
from typing import Callable

from pydantic import EmailStr, BaseModel

from quickflow.consts import AvailableModules
from quickflow.external_actions.chain.models import MailAction
from quickflow.external_actions.strategy.base import AbstractServiceStrategy


class EmailSchema(BaseModel):
    content: str
    attachments: dict[str, bytes]


class BaseMailStrategy(AbstractServiceStrategy, ABC):

    module_name: AvailableModules = AvailableModules.MAIL
    actions = MailAction

    def get_action_to_function_mapper(self) -> dict[MailAction, Callable]:
        return {
            MailAction.SEND: self.send_mail,
            MailAction.GET_FROM_ADDRESS: self.get_last_mail,
        }

    @abstractmethod
    def get_last_mail(self, from_address: EmailStr) -> EmailSchema | None:
        raise NotImplementedError

    @abstractmethod
    def send_mail(self, attachments: list):
        raise NotImplementedError
