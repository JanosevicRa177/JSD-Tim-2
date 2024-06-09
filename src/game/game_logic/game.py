import threading
import time

from game.game_logic.model.bonus.base_bonus import BaseBonus
from game.game_logic.model.bonus.default_bonus import DefaultBonus
from pytube import YouTube
from pydub import AudioSegment
import pygame
import os

class Game:
    instance = None
    gui = None

    bpm_speed = None
    score = 0
    bonus: BaseBonus | None = None
    current_move = None
    correct_action: bool | None = None
    restarting = False

    actions = []

    def __new__(cls, gui=None):
        if cls.instance is None:
            cls.instance = super(Game, cls).__new__(cls)
            cls.instance.gui = gui
        return cls.instance

    def start(self, level):
        self.bpm_speed = 60 / level.bpm
        self.restarting = False
        self.play_music(level.songUrl, level.songName)

        for command in level.commands:
            command.run_command()

        return

    def play_music(self, url, songName):
        file_path = self.download_file(url, songName)
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)  # -1 znači da se pesma ponavlja beskonačno

    def download_file(self, url, songName):
        # Skidanje videa sa yt i konverzija u mp3
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        downloaded_file = stream.download()
        file_path = os.path.join("songs", songName + ".mp3")
        audio = AudioSegment.from_file(downloaded_file)
        audio.export(file_path, format="mp3")
        os.remove(downloaded_file)
        return file_path

    def do_move(self, move):
        if self.gui.game_thread.stopped():
            return

        self.actions = []
        self.current_move = move
        self.correct_action = None
        self.gui.next_move(move.combination)

        t = threading.Thread(self.validate_move())
        t.start()
        t.join()

        self.gui.update_score(self.score)
        time.sleep(self.bpm_speed-0.5)

        self.lower_bonus_moves()

        return self.correct_action

    def run_pause(self):
        if self.gui.game_thread.stopped():
            return
        time.sleep(self.bpm_speed)

    def restart(self, level):
        self.restarting = True
        self.score = 0
        self.bonus = None

        self.start(level)

        if not self.gui.game_thread.stopped():
            self.gui.show_total_score(self.score)
        return

    def validate_move(self):
        time.sleep(0.5)
        if self.correct_action is not None:
            return

        if self.actions:
            sorted_actions = sorted(self.actions, key=len)
            if (self.current_move
                    and set(sorted_actions[-1]) == set(self.current_move.combination)):
                self.correct_action = True
            else:
                self.correct_action = False

        self.add_score()

    def add_score(self):
        if self.correct_action:
            self.score += 1 * self.get_bonus_multiplier()

    def add_bonus(self, bonus_moves: int):
        if self.bonus is None:
            self.bonus = DefaultBonus(bonus_moves)
        else:
            new_bonus = DefaultBonus(bonus_moves)
            new_bonus.bonus = self.bonus
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
                self.bonus = self.bonus.get_inner_bonus()
