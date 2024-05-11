from typing import Any

from game_logic.command import Command


class IfComplete(Command):

    def __init__(self, moves_with_bonus: int):
        self.moves_with_bonus = moves_with_bonus
        self.commands: list[Command] = []

    def get_combination(self) -> list[Any]:
        pass

    def get_multiplier(self) -> float:
        return 1

    def is_regular_move(self) -> bool:
        return False
