import string

from game_logic.game import Game
from game_logic.model.command import Command


class Move(Command):

    def __init__(self, move):
        self.combination: list[string] = []
        if "right" in move:
            self.combination.append("right")
        if "left" in move:
            self.combination.append("left")
        if "up" in move:
            self.combination.append("up")
        if "down" in move:
            self.combination.append("down")

    def run_command(self):
        game = Game(None)
        game.do_move(self)

    def is_regular_move(self) -> bool:
        return True
