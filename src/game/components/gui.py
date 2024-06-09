import tkinter as tk
from PIL import Image, ImageTk

from src.game.game_logic.game import Game
from .interface import Interface
from src.game.game_logic.model.level import Level
import keyboard

from .game_thread import GameThread


class TkinterGui(Interface):
    window = tk.Tk()
    levels: list[Level] = []
    current_level: Level = None
    keyboard_listener_initiated = False
    game_thread: GameThread | None = None
    even_command: False

    def __init__(self, levels):
        super().__init__()
        self.levels = levels
        self.even_command = False
        self.game = Game(self)

        self.window.title("JSD-Tim-2")
        self.window.state('zoomed')

        self.level_sidebar = tk.Frame(self.window, bg="red")
        self.level_playground = tk.Frame(self.window, bg="white")

        self.level_sidebar.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.level_playground.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

        self.level_sidebar.columnconfigure(0, weight=1)

        self.score_label = tk.Label(self.level_playground, text="0")
        self.score_label.pack()

        self.images_frame = tk.Frame(self.level_playground, bg='green')
        self.images_frame.place(x=0, rely=0.1, relheight=0.4, relwidth=1)

        self.images_frame.rowconfigure(0, weight=1)

        self.images_frame.columnconfigure(0, weight=1)
        self.images_frame.columnconfigure(1, weight=1)
        self.images_frame.columnconfigure(2, weight=1)
        self.images_frame.columnconfigure(3, weight=1)

        img_up, arrow_up, canvas_up = self.create_arrow_image_object('imgs/arrow-up.jpg', 0, 0)
        self.canvas_up = canvas_up

        img_left, arrow_left, canvas_left = self.create_arrow_image_object('imgs/arrow-left.jpg', 0, 1)
        self.canvas_left = canvas_left

        img_right, arrow_right, canvas_right = self.create_arrow_image_object('imgs/arrow-right.jpg', 0, 2)
        self.canvas_right = canvas_right

        img_down, arrow_down, canvas_down = self.create_arrow_image_object('imgs/arrow-down.jpg', 0, 3)
        self.canvas_down = canvas_down

        self.window.bind('<Key>', lambda e: self.key_pressed(e))

        self.initiate()

    def __del__(self):
        self.game_thread.stop()

    def create_arrow_image_object(self, img_path, row=0, column=0):
        img = Image.open(img_path)
        img = img.resize((200, 200))
        arrow = ImageTk.PhotoImage(img)
        canvas = tk.Canvas(self.images_frame, width=200, height=200, bg='lightblue')
        canvas.grid(row=row, column=column)
        canvas.create_image(0, 0, anchor=tk.NW, image=arrow)
        return img, arrow, canvas

    def key_pressed(self, event):
        combination = []
        if not self.keyboard_listener_initiated:
            keyboard.press("shift")
            keyboard.release("shift")
            self.keyboard_listener_initiated = True
        combination.extend(['up'] if keyboard.is_pressed('up') else [])
        combination.extend(['down'] if keyboard.is_pressed('down') else [])
        combination.extend(['left'] if keyboard.is_pressed('left') else [])
        combination.extend(['right'] if keyboard.is_pressed('right') else [])
        if self.game and len(combination) > 0:
            self.game.actions.append(combination)

    def next_move(self, directions):
        self.toggle_canvas('up', directions, 0, 0)
        self.toggle_canvas('left', directions, 0, 1)
        self.toggle_canvas('right', directions, 0, 2)
        self.toggle_canvas('down', directions, 0, 3)
        if self.even_command:
            self.images_frame.configure(bg='green')
        else:
            self.images_frame.configure(bg='blue')
        self.even_command = not self.even_command
        self.window.update()

    def toggle_canvas(self, toggle_name, directions, row, column):
        prop_name = 'canvas_{}'.format(toggle_name)
        condition = toggle_name in directions
        attr = getattr(self, prop_name)
        attr.grid(row=row, column=column) if condition else attr.grid_forget()

    def initiate(self):
        self.draw()
        self.window.mainloop()

    def draw(self):
        self.__draw_levels()

    def __draw_levels(self) -> None:
        for idx, level in enumerate(self.levels):
            k = idx + 1
            btn = tk.Button(self.level_sidebar, height=2,
                            bg="blue", fg="white", font=10, text=str(k) + " " + level.songName,
                            command=lambda lvl=level, lvl_ind=k: self.start_level(lvl))
            btn.grid(row=idx, column=0, sticky='nsew')

    def start_level(self, level: Level) -> None:
        self.score_label.config(text="Your score is 0")
        if self.game_thread is not None:
            self.game_thread.stop()
            self.show_total_score(self.game.score)
            self.game_thread.join()
        self.game_thread = GameThread(target=self.game.restart, args=(level,))
        self.game_thread.start()

    def update_score(self, score):
        self.score_label.config(text="Your score is {}".format(score))
        self.score_label.update()
        self.window.update()

    def show_total_score(self, score):
        self.score_label.config(text="Your total score is {}".format(self.game.score))


