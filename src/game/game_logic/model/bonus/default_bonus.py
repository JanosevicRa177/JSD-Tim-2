from typing import Optional

from game.game_logic.model.bonus.base_bonus import BaseBonus


class DefaultBonus(BaseBonus):

    bonus: BaseBonus | None = None

    def __init__(self, bonus_moves):
        self.bonus_moves = bonus_moves

    def get_bonus_multiplier(self):
        if self.bonus is None:
            return 1.1
        else:
            return round(1.1 * self.bonus.get_bonus_multiplier(), 2)

    def add_bonus(self, bonus_moves: int):
        if self.bonus is None:
            self.bonus = DefaultBonus(bonus_moves)
            return
        self.bonus.add_bonus(bonus_moves)

    def lower_bonus_moves(self):
        self.bonus_moves -= 1
        if self.bonus is not None:
            self.bonus.lower_bonus_moves()
            if self.bonus.get_bonus_moves() <= 0:
                self.bonus = self.bonus.get_inner_bonus()

    def get_bonus_moves(self):
        return self.bonus_moves

    def get_inner_bonus(self) -> Optional['BaseBonus']:
        return self.bonus
