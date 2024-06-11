import os
from gme.components import TkinterGui
from gme.game_logic.model.level import Level
from textx import metamodel_from_file


entity_mm = metamodel_from_file('gme/grammar.tx')


def scan_level_files():
    level_files = []
    for file in os.listdir("gme/levels"):
        if file.endswith(".gme"):
            level_files.append(os.path.join("gme/levels", file))
    return level_files


def load_level_model(file_path):
    model = entity_mm.model_from_file(file_path)
    level = Level(model)
    return level


def load_levels():
    level_files = scan_level_files()
    return [load_level_model(level_file) for level_file in level_files]


def main():
    levels = load_levels()

    gui = TkinterGui(levels)
    gui.initiate()


if __name__ == "__main__":
    main()
