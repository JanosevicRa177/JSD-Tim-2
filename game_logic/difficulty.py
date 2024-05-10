import string
from typing import Any

from game_logic.command import Command


class Difficulty(Command):

    def __init__(self, name: string, value: float):
        self.name = name
        self.value = value

    def get_combination(self) -> list[Any]:
        pass

    def get_multiplier(self) -> float:
        return 1

    def is_regular_move(self) -> bool:
        return False
