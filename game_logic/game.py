from game_logic.action import Action
from interpret_model import Level
import threading

from collections import deque


class Game:
    level: Level = None
    is_locked = False
    should_stop = False
    current_moves: deque[Action] = deque()
    current_move = None
    score = 0
    multiplier = 1
    timer = None

    correct_action = 0

    def __init__(self, observer):
        self.observer = observer

    def start(self):
        self.timer = threading.Timer(5.0, self.start)
        self.timer.start()

        if self.should_stop:
            return

        if len(self.current_moves) == 0:
            self.should_stop = True
            return
        self.update_parameters()
        self.current_move = self.current_moves.popleft()
        self.observer.process_action(self.current_move)

    def __del__(self):
        self.should_stop = True

    def restart(self, level, moves):
        self.level = level
        self.current_moves = deque()
        self.score = 0
        self.multiplier = 1

        if self.timer:
            self.timer.cancel()
            self.timer = threading.Timer(2.0, self.start)

        for move in moves:
            self.current_moves.append(move)
        self.start()

    def validate_action(self, combination):
        if self.current_move \
                and set(combination) == set(self.current_move.get_combination()):
            print('Action is correct', combination, self.current_move.get_combination())
            self.correct_action = 1
            return
        print('Action is incorrect', self.current_move.get_combination())
        self.correct_action = 0

    def update_parameters(self):
        if not self.current_move:
            return
        self.multiplier *= self.current_move.get_multiplier()
        self.score += self.correct_action * self.multiplier
        print('New Score {}, New Multiplier {}'.format(self.score, self.multiplier))
