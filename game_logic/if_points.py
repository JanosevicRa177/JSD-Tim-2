from typing import Any

from game_logic.command import Command


class IfPoints(Command):

    def __init__(self, points: int, moves_with_bonus: int):
        self.points = points
        self.moves_with_bonus = moves_with_bonus

    def get_combination(self) -> list[Any]:
        pass

    def get_multiplier(self) -> float:
        return 1

    def is_regular_move(self) -> bool:
        return False
