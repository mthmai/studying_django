from abc import ABC, abstractmethod


class ViewsABC(ABC):

    @abstractmethod
    def validator(self) -> bool:
        ...

    @abstractmethod
    def request_page(self) -> None:
        ...

    