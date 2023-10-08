from abc import abstractmethod


class BaseMailStrategy:

    @abstractmethod
    def get_mail(self):
        raise NotImplementedError

    @abstractmethod
    def send_mail(self, attachments: list):
        raise NotImplementedError
