import tkinter as tk

class Menu():
    def __init__(self, master):
        self.master = master
        self.menu_frame = tk.Frame(self.master.root)
        self.output = tk.Label(self.menu_frame, text = 'A', bg = "yellow")
        self.train_button = tk.Button(self.menu_frame, text = 'Trenuj siec')
        self.recognize_button = tk.Button(self.menu_frame, text = 'Rozpoznaj')
        self.clear_button = tk.Button(self.menu_frame, text = 'Wyczysc', command = lambda: self.clear())
        self.relheight = 0.2
        self.relwidth = 0.9
        self.button_width = 0.2
        self.button_height = 0.2
        self.offset = (1-(3*self.button_width+0.3))/3

    def train(self):
        pass

    def recognize(self):
        pass

    def clear(self):
        self.master.drawing_box.clear()

    def place(self):
        self.menu_frame.place(relx = (1-self.relwidth)/2, rely = 0.6, relwidth = self.relwidth, relheight = self.relheight)
        self.train_button.place(rely = (1-self.button_height)/2, relwidth = self.button_width, relheight = self.button_height)
        self.recognize_button.place(relx = (self.button_width+self.offset)*1, rely = (1-self.button_height)/2, relwidth = self.button_width, relheight = self.button_height)
        self.clear_button.place(relx = (self.button_width+self.offset)*2, rely = (1-self.button_height)/2, relwidth = self.button_width, relheight = self.button_height)
        self.output.place(relx = 0.7, relwidth = 0.3, relheight = 1)

class DrawingBox():
    def __init__(self, master):
        self.master = master
        self.drawing_frame = tk.Frame(self.master.root, bg = 'blue')
        self.title = tk.Label(self.drawing_frame, text = 'Narysuj litere')
        self.canvas_width = 250
        self.canvas_height = 250
        self.canvas = tk.Canvas(self.drawing_frame, width = self.canvas_width, height = self.canvas_height, bg = 'white')
        self.relheight = 0.5
        self.relwidth = 0.6
        self.img_width = 50
        self.img_height = 50
        self.board = [[0]*self.img_width]*self.img_height
        self.canvas.bind('<B1-Motion>', self.paint)

    def clear(self):
        for y in range(self.img_height):
            for x in range(self.img_width):
                self.board[y][x] = 0
        self.canvas.delete("all")

    def paint(self, e):
        cell_width = self.canvas_width/self.img_width
        cell_height = self.canvas_height/self.img_height
        x = int(e.x/cell_width)
        y = int(e.y/cell_height)
        self.board[y][x] = 1
        self.canvas.create_rectangle(x*cell_width, y*cell_height, (x+1)*cell_width, (y+1)*cell_height, fill = "black")

    def place(self):
        self.drawing_frame.place(relx = (1-self.relwidth)/2, rely = 0.05, relwidth = self.relwidth, relheight = self.relheight)
        self.title.place(relwidth = 1, relheight = 0.1)
        self.canvas.place(rely = 0.1)

class Window():
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x600")
        self.drawing_box = DrawingBox(self)
        self.menu = Menu(self)
        self.place()
    
    def place(self):
        self.drawing_box.place()
        self.menu.place()