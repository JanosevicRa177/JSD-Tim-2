import time

from game_logic.model.bonus.base_bonus import BaseBonus
from game_logic.model.bonus.default_bonus import DefaultBonus

import copy


class Game:
    instance = None
    gui = None

    bpm_speed = 0
    score = 0
    bonus: BaseBonus | None = None
    current_move = None
    correct_action: bool | None = None

    def __new__(cls, gui=None):
        if cls.instance is None:
            cls.instance = super(Game, cls).__new__(cls)
            cls.instance.gui = gui
        return cls.instance

    def start(self, level):
        self.bpm_speed = 60 / level.bpm

        for command in level.commands:
            command.run_command()

        self.gui.show_total_score()
        return

    def do_move(self, move):
        self.current_move = move
        self.correct_action = None
        self.gui.next_move(move.combination)
        time.sleep(self.bpm_speed)
        return self.correct_action

    def restart(self, level):
        self.score = 0
        self.bonus = None
        self.start(level)

    def validate_move(self, combination):
        if self.correct_action is not None:
            return

        if (self.current_move
                and set(combination) == set(self.current_move.combination)):
            self.correct_action = True
        else:
            self.correct_action = False

        self.add_score()
        self.gui.update_score(self.score)

    def add_score(self):
        if self.correct_action:
            self.score += 1 * self.get_bonus_multiplier()

    def add_bonus(self, bonus_moves: int):
        new_bonus = DefaultBonus(bonus_moves)
        if self.bonus is None:
            self.bonus = DefaultBonus(bonus_moves)
        else:
            new_bonus.bonus = copy.copy(self.bonus)
            self.bonus = new_bonus

    def get_bonus_multiplier(self):
        if self.bonus is None:
            return 1
        else:
            return round(self.bonus.get_bonus_multiplier(), 2)

    def lower_bonus_moves(self):
        if self.bonus is not None:
            self.bonus.lower_bonus_moves()
            if self.bonus.get_bonus_moves() <= 0:
                if self.bonus.get_inner_bonus() is not None:
                    self.bonus = self.bonus.get_inner_bonus()
                else:
                    self.bonus = None
