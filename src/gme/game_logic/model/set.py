import string

from gme.game_logic.model.command import Command


class Set(Command):

    def __init__(self, name: string):
        self.name = name
        self.commands: list[Command] = []

    def run_command(self):
        for command in self.commands:
            command.run_command()
        return True

    def is_regular_move(self) -> bool:
        return False
