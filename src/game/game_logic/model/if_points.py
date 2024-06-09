from game.game_logic.game import Game
from game.game_logic.model.command import Command


class IfPoints(Command):

    def __init__(self, points: int, moves_with_bonus: int):
        self.moves_with_bonus = moves_with_bonus
        self.points = points

    def run_command(self):
        game = Game()
        if game.score >= self.points:
            game.bonus.add_bonus(self.moves_with_bonus)

    def is_regular_move(self) -> bool:
        return False
