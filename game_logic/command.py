from abc import ABC, abstractmethod
from typing import Any


class Command(ABC):

    @abstractmethod
    def get_combination(self) -> list[Any]:
        pass

    @abstractmethod
    def get_multiplier(self) -> float:
        pass

    @abstractmethod
    def is_regular_move(self) -> bool:
        pass
