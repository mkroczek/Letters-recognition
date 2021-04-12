import tkinter as tk
import tkinter.ttk as ttk
# from src.model import Model
from src.MLP import MLP
from src.data_set import DataManager
import numpy as np
import os
import io
from PIL import Image


class Menu():
    def __init__(self, master):
        self.master = master
        self.menu_frame = tk.Frame(self.master.root)
        self.output = tk.Label(self.menu_frame, bg='yellow', width=10, height=5)
        self.letter_buttons = list()
        for letter in self.master.categories:
            self.letter_buttons.append(ttk.Button(self.menu_frame, text=letter, command=lambda letter = letter: self.choose(letter)))
        self.save_button = ttk.Button(self.menu_frame, text='Zapisz', command=lambda: self.save())
        # self.clear_button = ttk.Button(self.menu_frame, text='Wyczysc', command=lambda: self.clear())

    def choose(self, letter):
        self.output.config(text = letter)

    def save(self):
        number = 0
        letter = self.output.cget('text')
        directory = self.master.save_directory
        if not os.path.isdir(directory):
            os.mkdir(directory)
        directory = os.path.join(self.master.save_directory, letter)
        data = np.array(self.master.drawing_box.board, dtype = np.uint8)
        img = Image.fromarray(data)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        while os.path.exists(os.path.join(directory, f'{number}.png')):
            number += 1
        img.save(os.path.join(directory, f'{number}.png'))
        self.clear()

    def clear(self):
        self.master.drawing_box.clear()
        self.output.config(text="")

    def place(self):
        self.menu_frame.grid(row=1, column=0, pady=30, padx=30)
        for i in range(len(self.letter_buttons)):
            self.letter_buttons[i].grid(row = int(i/3), column = i%3)
        self.save_button.grid(row=1, column=3)
        self.output.grid(row=0, column=3, padx=5)


class DrawingBox():
    def __init__(self, master):
        self.master = master
        self.drawing_frame = tk.Frame(self.master.root)
        self.title = ttk.Label(self.drawing_frame, text='Narysuj litere')
        self.canvas_width = 250
        self.canvas_height = 250
        self.canvas = tk.Canvas(self.drawing_frame, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.img_width = 30
        self.img_height = 30
        # self.img_width = 28
        # self.img_height = 28
        self.board = [[255.0] * self.img_width for i in range(self.img_height)]
        self.canvas.bind('<B1-Motion>', self.paint)

    def clear(self):
        for y in range(self.img_height):
            for x in range(self.img_width):
                self.board[y][x] = 255.0
        self.canvas.delete("all")

    def paint(self, e):
        cell_width = self.canvas_width / self.img_width
        cell_height = self.canvas_height / self.img_height
        x = int(e.x / cell_width)
        y = int(e.y / cell_height)
        self.board[y][x] = 0.0
        self.canvas.create_rectangle(x * cell_width, y * cell_height, (x + 1) * cell_width, (y + 1) * cell_height,
                                     fill="black")

    def place(self):
        self.drawing_frame.grid(row=0, column=0, padx=30, pady=30)
        self.title.grid(row=0, pady=5)
        self.canvas.grid(row=1, column=0)


class Window():
    def __init__(self, root):
        self.categories = ["I", "O", "U", "W", "X"]
        self.save_directory = "Letters_gui"
        self.root = root
        self.drawing_box = DrawingBox(self)
        self.menu = Menu(self)
        self.place()

    def place(self):
        self.drawing_box.place()
        self.menu.place()

root = tk.Tk()
app = Window(root)
root.wm_title("Data creation tool")
root.mainloop()