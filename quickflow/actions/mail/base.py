from abc import abstractmethod, ABC


class BaseMailStrategy(ABC):
    @abstractmethod
    def get_mail(self):
        raise NotImplementedError

    @abstractmethod
    def send_mail(self, attachments: list):
        raise NotImplementedError
