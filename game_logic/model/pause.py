from game_logic.model.command import Command


class Pause(Command):

    def __init__(self, value: int):
        self.value = value

    def run_command(self):
        return True

    def is_regular_move(self) -> bool:
        return False
