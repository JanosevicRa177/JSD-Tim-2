from src.gme.game_logic.game import Game
from src.gme.game_logic.model.command import Command


class IfComplete(Command):

    def __init__(self, moves_with_bonus: int):
        self.moves_with_bonus = moves_with_bonus
        self.commands: list[Command] = []

    def run_command(self):
        successful_moves = 0
        for command in self.commands:
            move_successful = command.run_command()
            if move_successful and command.is_regular_move():
                successful_moves += 1
        filtered_commands = [command for command in self.commands if command.is_regular_move()]
        if len(filtered_commands) == successful_moves:
            game = Game()
            game.add_bonus(self.moves_with_bonus)
        return True

    def is_regular_move(self) -> bool:
        return False
