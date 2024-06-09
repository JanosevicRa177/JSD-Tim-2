from src.game_logic.game import Game
from src.game_logic.model.command import Command


class Pause(Command):

    def __init__(self, value: int):
        self.value = value

    def run_command(self):
        game = Game()
        for i in range(self.value):
            game.run_pause()

    def is_regular_move(self) -> bool:
        return False
