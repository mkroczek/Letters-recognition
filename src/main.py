#from window import Window
from window import Window
import tkinter as tk

root = tk.Tk()
app = Window(root)
root.wm_title("Letters recognition")
root.mainloop()