from typing import Optional

from game_logic.model.bonus.base_bonus import BaseBonus


class DefaultBonus(BaseBonus):

    bonus: BaseBonus | None = None

    def __init__(self, bonus_moves):
        self.bonus_moves = bonus_moves

    def get_bonus_multiplier(self) -> float:
        multiplier = 1.1
        if self.bonus is not None:
            multiplier *= self.bonus.get_bonus_multiplier()
        return round(multiplier, 2)

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
