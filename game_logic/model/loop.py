from game_logic.model.command import Command


class Loop(Command):

    def __init__(self, times_to_repeat: int):
        self.times_to_repeat = times_to_repeat
        self.commands: list[Command] = []

    def run_command(self):
        for _ in range(self.times_to_repeat):
            for command in self.commands:
                command.run_command()

    def is_regular_move(self) -> bool:
        return False
