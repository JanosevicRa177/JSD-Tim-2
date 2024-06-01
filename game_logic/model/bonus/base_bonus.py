from abc import ABC, abstractmethod
from typing import Optional


class BaseBonus(ABC):
    @abstractmethod
    def get_bonus_multiplier(self):
        pass

    @abstractmethod
    def lower_bonus_moves(self):
        pass

    @abstractmethod
    def get_bonus_moves(self):
        pass

    @abstractmethod
    def get_inner_bonus(self) -> Optional['BaseBonus']:
        pass
