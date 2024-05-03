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
        self.images_frame.place(x=0, rely=0.2, relheight=0.4, relwidth=1)

        self.images_frame.rowconfigure(0, weight=1)
        self.images_frame.columnconfigure((0, 1, 2, 3), weight=1)

        img_left = Image.open('imgs/arrow-left.jpg')
        img_left = img_left.resize((200, 200))
        arrow_left = ImageTk.PhotoImage(img_left)
        canvas_left = tk.Canvas(self.images_frame, width=200, height=200, bg='lightblue')
        canvas_left.grid(row=0, column=0)
        canvas_left.create_image(0, 0, anchor=tk.NW, image=arrow_left)
        self.canvas_left = canvas_left

        img_right = Image.open('imgs/arrow-right.jpg')
        img_right = img_right.resize((200, 200))
        arrow_right = ImageTk.PhotoImage(img_right)
        canvas_right = tk.Canvas(self.images_frame, width=200, height=200, bg='lightblue')
        canvas_right.grid(row=0, column=1)
        canvas_right.create_image(0, 0, anchor=tk.NW, image=arrow_right)
        self.canvas_right = canvas_right

        img_up = Image.open('imgs/arrow-up.jpg')
        img_up = img_up.resize((200, 200))
        arrow_up = ImageTk.PhotoImage(img_up)
        canvas_up = tk.Canvas(self.images_frame, width=200, height=200, bg='lightblue')
        canvas_up.grid(row=0, column=2)
        canvas_up.create_image(0, 0, anchor=tk.NW, image=arrow_up)
        self.canvas_up = canvas_up

        img_down = Image.open('imgs/arrow-down.jpg')
        img_down = img_down.resize((200, 200))
        arrow_down = ImageTk.PhotoImage(img_down)
        canvas_down = tk.Canvas(self.images_frame, width=200, height=200, bg='lightblue')
        canvas_down.grid(row=0, column=3)
        canvas_down.create_image(0, 0, anchor=tk.NW, image=arrow_down)
        self.canvas_down = canvas_down
        self.canvas_down.grid_forget()
        self.initiate(levels)


    def create_arrow_image_object(self, img_path):
        img = Image.open(img_path)
        img = img.resize((200, 200))
        img.show()
        arrow_down = ImageTk.PhotoImage(img)
        canvas = tk.Canvas(self.images_frame, width=200, height=200, bg='lightblue')
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=arrow_down)
        return canvas
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
