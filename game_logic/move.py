from typing import Any

from game_logic.action import Action


class Move(Action):
    def __init__(self, combination):
        self.combination = combination

    def get_combination(self) -> list[Any]:
        return self.combination

    def get_multiplier(self) -> float:
        return 1

    def is_regular_move(self):
        return True
