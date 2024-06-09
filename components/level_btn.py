import tkinter as tk


class LevelBtn(tk.Button):
    def __init__(self, window, text, command, i, j, padx=5, pady=5):
        super().__init__(window, text=text, width=5, height=1, command=command, background='blue', fg='white', font=20)
        # self.grid(row=i, column=j, padx=padx, pady=pady)
        self.pack(pady=pady)