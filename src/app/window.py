import tkinter as tk
import tkinter.ttk as ttk
from src.network.MLP import MLP
from src.network.data_set import DataManager
from src.utils.json_export import *
import numpy as np

class Menu():
    def __init__(self, master):
        self.master = master
        self.menu_frame = tk.Frame(self.master.root)
        self.output = tk.Label(self.menu_frame, bg = '#a8cca7', width = 6 ,height = 3, font = 20)
        self.recognize_button = ttk.Button(self.menu_frame, text = 'Rozpoznaj', command = lambda: self.recognize())
        self.clear_button = ttk.Button(self.menu_frame, text = 'Wyczysc', command = lambda: self.clear())
        self.export_button = ttk.Button(self.menu_frame, text = 'Zapisz', command = lambda: self.export_json())
        self.train_button = ttk.Button(self.menu_frame, text = 'Trenuj siec', command = lambda: self.train())
        self.import_button = ttk.Button(self.menu_frame, text = 'Wczytaj', command = lambda: self.import_json())

    def train(self):
        self.master.model.train()
        x, y = self.master.data_manager.create_test_data(self.master.test_data_path)
        print(f"Trained network has accuracy: {self.master.model.evaluate_network(x, y)}")

    def export_json(self):
        export_to_json(self.master.model.network)

    def import_json(self):
        self.master.model.set_network(import_from_json())
        x, y = self.master.data_manager.create_test_data(self.master.test_data_path)
        print(f"Imported network has accuracy: {self.master.model.evaluate_network(x, y)}")

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
        self.menu_frame.grid(row = 1, column = 0, padx = 30)
        self.import_button.grid(row = 0, column = 0, padx = 5)
        self.train_button.grid(row = 0, column = 1, padx = 5)
        self.export_button.grid(row = 0, column = 2, padx = 5)
        self.recognize_button.grid(row = 1, column = 0, padx = 5)
        self.clear_button.grid(row = 1, column = 1, padx = 5)
        self.output.grid(row = 1, column = 2, padx = 5, pady = 20)

class DrawingBox():
    def __init__(self, master):
        self.master = master
        self.drawing_frame = tk.Frame(self.master.root)
        self.title = ttk.Label(self.drawing_frame, text = 'Narysuj litere')
        self.canvas_width = 250
        self.canvas_height = 250
        self.canvas = tk.Canvas(self.drawing_frame, width = self.canvas_width, height = self.canvas_height, bg = 'white')
        self.img_width = self.master.img_size
        self.img_height = self.master.img_size
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
        self.img_size = 15
        self.data_manager = DataManager("Letters_gui", self.categories, self.img_size)
        self.test_data_path = 'Letters_gui_test'
        self.model = MLP(self.data_manager.create_training_set(), len(self.categories))
        self.root = root
        self.drawing_box = DrawingBox(self)
        self.menu = Menu(self)
        self.place()
    
    def place(self):
        self.drawing_box.place()
        self.menu.place()