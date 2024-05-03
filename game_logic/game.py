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
    multiplier = 0
    timer = None

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

        self.current_move = self.current_moves.popleft()
        self.observer.process_action(self.current_move)

    def __del__(self):
        self.should_stop = True

    def restart(self, level, moves):
        self.level = level
        self.current_moves = deque()
        self.score = 0
        self.multiplier = 0

        if self.timer:
            self.timer.cancel()
            self.timer = threading.Timer(2.0, self.start)

        for move in moves:
            self.current_moves.append(move)
        self.start()

    def update_parameters(self, action):
        self.multiplier *= action.get_multiplier()
        self.score += action.get_score()
        print('New Score {}, New Multiplier {}'.format(self.score, self.multiplier))


