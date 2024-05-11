from typing import Any

from game_logic.command import Command


class EndBonusSequence(Command):
    def __init__(self, multiplier):
        self.multiplier = multiplier
    def get_combination(self) -> list[Any]:
        return []

    def get_multiplier(self) -> float:
        return 1/self.multiplier

    def is_regular_move(self) -> bool:
        return False


