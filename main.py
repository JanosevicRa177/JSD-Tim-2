from textx.metamodel import metamodel_from_file

from components.gui import TkinterGui
from components.interface import Interface
from game import Game
from interpret_model import Level
import os

entity_mm = metamodel_from_file('grammar.tx')


def scan_level_files():
    level_files = []
    for file in os.listdir("levels"):
        if file.endswith(".ddr"):
            level_files.append(os.path.join("levels", file))
    return level_files


def load_level_model(file_path):
    model = entity_mm.model_from_file(file_path)
    level = Level(debug=False)
    level.interpret_level(model)
    return level


def load_levels():
    level_files = scan_level_files()
    return [load_level_model(level_file) for level_file in level_files]


if __name__ == "__main__":
    levels = load_levels()
    gui: Interface = TkinterGui(levels)
    # game = Game()
