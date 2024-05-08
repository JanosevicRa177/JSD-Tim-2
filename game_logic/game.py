from game_logic.command import Command
from game_logic.endmove import EndMove
from game_logic.move import Move
from interpret_model import Level
import threading

from collections import deque


class Game:
    level: Level = None
    is_locked = False
    should_stop = False
    current_moves: deque[Command] = deque()
    current_move = None
    score = 0
    multiplier = 1
    timer = None
    speed = 3.0
    correct_action = -1

    def __init__(self, observer):
        self.gui = observer

    def start(self):
        self.timer = threading.Timer(self.speed, self.start)
        self.timer.start()

        if self.should_stop:
            self.timer.cancel()
            self.gui.show_total_score()
            return

        self.update_parameters()
        self.current_move = self.current_moves.popleft()
        self.gui.process_action(self.current_move)

        self.correct_action = -1

        if not self.current_move.is_regular_move():
            self.timer.cancel()
            self.start()

        if len(self.current_moves) == 0:
            self.should_stop = True
            self.gui.show_total_score()
            return

    def __del__(self):
        self.should_stop = True

    def restart(self, level, moves):
        print('restarting')
        self.level = level
        self.current_moves = deque()
        self.score = 0
        self.multiplier = 1
        self.correct_action = -1

        if self.timer:
            self.timer.cancel()
            self.timer = threading.Timer(self.speed, self.start)

        for move in moves:
            self.current_moves.append(move)
        self.current_moves.append(EndMove())
        self.should_stop = False
        self.start()

    def validate_action(self, combination):
        if self.correct_action in [0, 1]:
            return

        if (self.current_move
                and set(combination) == set(self.current_move.get_combination())):
            self.correct_action = 1
        else:
            self.correct_action = 0

        self.update_score()
        self.gui.update_score(self.score)

    def update_parameters(self):
        if not self.current_move:
            return
        self.calculate_multiplier()
        print('New Score {}, New Multiplier {}'.format(self.score, self.multiplier))

    def update_score(self):
        self.score += self.correct_action * self.multiplier

    def calculate_multiplier(self):
        self.multiplier *= self.current_move.get_multiplier()
