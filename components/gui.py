import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from .interface import Interface
from interpret_model import Level


class TkinterGui(Interface):
    window = tk.Tk()
    levels: list[Level] = []

    def __init__(self, levels):
        super().__init__()
        self.window.title("JSD-Tim-2")
        self.window.state('zoomed')

        self.level_sidebar = tk.Frame(self.window, bg="red")
        self.level_playground = tk.Frame(self.window, bg="white")

        self.level_sidebar.place(x=0, y=0, relwidth=0.3, relheight=1)
        self.level_playground.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

        self.level_sidebar.columnconfigure(0, weight=1)

        self.images_frame = tk.Frame(self.level_playground, bg='green')
        self.images_frame.place(x=0, rely=0.1, relheight=0.4, relwidth=1)

        self.images_frame.rowconfigure(0, weight=1)
        self.images_frame.columnconfigure((0, 1, 2, 3), weight=1)

        img_up, arrow_up, canvas_up = self.create_arrow_image_object('imgs/arrow-up.jpg', 0, 0)
        self.canvas_up = canvas_up

        img_left, arrow_left, canvas_left = self.create_arrow_image_object('imgs/arrow-left.jpg', 0, 1)
        self.canvas_left = canvas_left

        img_right, arrow_right, canvas_right = self.create_arrow_image_object('imgs/arrow-right.jpg', 0, 2)
        self.canvas_right = canvas_right

        img_down, arrow_down, canvas_down = self.create_arrow_image_object('imgs/arrow-down.jpg', 0, 3)
        self.canvas_down = canvas_down

        self.initiate(levels)

    def create_arrow_image_object(self, img_path, row=0, column=0):
        img = Image.open(img_path)
        img = img.resize((200, 200))
        arrow = ImageTk.PhotoImage(img)
        canvas = tk.Canvas(self.images_frame, width=200, height=200, bg='lightblue')
        canvas.grid(row=row, column=column)
        canvas.create_image(0, 0, anchor=tk.NW, image=arrow)
        return img, arrow, canvas

    def initiate(self, levels):
        self.levels = levels
        self.draw()

    def draw(self):
        self.__draw_levels()
        self.window.mainloop()

    def __draw_levels(self) -> None:
        for idx, level in enumerate(self.levels):
            k = idx + 1
            btn = tk.Button(self.level_sidebar, height=2,
                            bg="blue", fg="white", font=10,text=str(k),
                            command=lambda lvl=level, lvl_ind=k: self.start_level(level))
            btn.grid(row=idx, column=0, sticky='nsew')

    def start_level(self, level: Level) -> None:
        print('Starting level {}'.format(level.points))
