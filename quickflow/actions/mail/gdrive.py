from abc import abstractmethod, ABC

from quickflow.actions.mail.base import BaseMailStrategy


class GMailStrategy(BaseMailStrategy, ABC):

    @abstractmethod
    def get_mail(self):
        ...

    @abstractmethod
    def send_mail(self, attachments: list):
        ...
