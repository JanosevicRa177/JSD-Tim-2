from threading import Thread

from interpret_model import Level
import time


class Game:
    score = 0
    is_paused = False

    def __init__(self, level: Level):
        self.level = level
        self.thread = Thread()

    def start(self, callback):
        self.thread = Thread(target=self.run, args=(callback,))
        self.thread.start()

    def stop(self):
        self.thread.join()

    def run(self, callback):
        while self.thread.is_alive():
            if not self.should_run():
                print('stopping the run')
                self.thread.join()
                continue
            callback()
            time.sleep(self.level.get_speed())

    def pause(self):
        self.is_paused = True

    def should_run(self):
        return not self.is_paused
