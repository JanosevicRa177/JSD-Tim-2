from typing import Any

from game_logic.command import Command


class Loop(Command):

    def __init__(self, times_to_repeat: int):
        self.times_to_repeat = times_to_repeat
        self.commands: list[Command] = []

    def get_combination(self) -> list[Any]:
        pass

    def get_multiplier(self) -> float:
        return 1

    def is_regular_move(self) -> bool:
        return False
