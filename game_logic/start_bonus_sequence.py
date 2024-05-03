from typing import Any

from game_logic.action import Action


class StartBonusSequence(Action):

    def __init__(self, multiplier):
        self.multiplier = multiplier

    def get_combination(self) -> list[Any]:
        return []

    def get_multiplier(self) -> float:
        return self.multiplier

    def is_regular_move(self):
        return False
