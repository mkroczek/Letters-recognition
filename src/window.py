import tkinter as tk
import tkinter.ttk as ttk
# from src.model import Model
from src.MLP import MLP
from src.data_set import DataManager
import numpy as np

class Menu():
    def __init__(self, master):
        self.master = master
        self.menu_frame = tk.Frame(self.master.root)
        self.output = tk.Label(self.menu_frame, bg = 'yellow', width = 10 ,height = 5)
        self.train_button = ttk.Button(self.menu_frame, text = 'Trenuj siec', command = lambda: self.train())
        self.recognize_button = ttk.Button(self.menu_frame, text = 'Rozpoznaj', command = lambda: self.recognize())
        self.clear_button = ttk.Button(self.menu_frame, text = 'Wyczysc', command = lambda: self.clear())

    def train(self):
        self.master.model.train()

    def recognize(self):
        img = self.master.drawing_box.board
        img = np.array(img)
        img = img.flatten()
        result = self.master.model.predict(img)
        self.output.config(text = self.master.categories[result])

    def clear(self):
        self.master.drawing_box.clear()
        self.output.config(text = "")

    def place(self):
        self.menu_frame.grid(row = 1, column = 0, pady = 30, padx = 30)
        self.train_button.grid(row = 0, column = 0, padx = 5)
        self.recognize_button.grid(row = 0, column = 1, padx = 5)
        self.clear_button.grid(row = 0, column = 2, padx = 5)
        self.output.grid(row = 0, column = 3, padx = 5)

class DrawingBox():
    def __init__(self, master):
        self.master = master
        self.drawing_frame = tk.Frame(self.master.root)
        self.title = ttk.Label(self.drawing_frame, text = 'Narysuj litere')
        self.canvas_width = 250
        self.canvas_height = 250
        self.canvas = tk.Canvas(self.drawing_frame, width = self.canvas_width, height = self.canvas_height, bg = 'white')
        self.img_width = 15
        self.img_height = 15
        # self.img_width = 28
        # self.img_height = 28
        self.board = [[0.0]*self.img_width for i in range(self.img_height)]
        self.canvas.bind('<B1-Motion>', self.paint)

    def clear(self):
        for y in range(self.img_height):
            for x in range(self.img_width):
                self.board[y][x] = 0.0
        self.canvas.delete("all")

    def paint(self, e):
        cell_width = self.canvas_width/self.img_width
        cell_height = self.canvas_height/self.img_height
        x = int(e.x/cell_width)
        y = int(e.y/cell_height)
        if (x < len(self.board) and y < len(self.board)):
            self.board[y][x] = 1.0
        self.canvas.create_rectangle(x*cell_width, y*cell_height, (x+1)*cell_width, (y+1)*cell_height, fill = "black")

    def place(self):
        self.drawing_frame.grid(row = 0, column = 0, padx = 30, pady = 30)
        self.title.grid(row = 0, pady = 5)
        self.canvas.grid(row = 1, column = 0)

class Window():
    def __init__(self, root):
        self.categories = ["I", "O", "U", "W", "X"]
        self.data_manager = DataManager("Letters_gui", self.categories, 15)
        self.model = MLP(self.data_manager.create_training_set(), len(self.categories))
        self.root = root
        self.drawing_box = DrawingBox(self)
        self.menu = Menu(self)
        self.place()
    
    def place(self):
        self.drawing_box.place()
        self.menu.place()