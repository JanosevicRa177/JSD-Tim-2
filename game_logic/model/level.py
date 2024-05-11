from game_logic.model.command import Command
from game_logic.model.converter.converter import interpret_command
from game_logic.model.difficulty import Difficulty


class Level:
    def __init__(self, model):
        self.commands: list[Command] = []
        self.difficulties: list[Difficulty] = []
        self.songName = model.songName
        self.bpm = model.bpm

        for difficulty in model.difficulty:
            difficulty_model = Difficulty(difficulty.name, difficulty.value)
            self.difficulties.append(difficulty_model)
        for command in model.commands:
            interpreted_command = interpret_command(command)
            self.commands.append(interpreted_command)
