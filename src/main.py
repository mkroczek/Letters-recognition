#from window import Window
from src.window import Window
import tkinter as tk
import os

os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices' #dzieki temu nie wywala bledu
root = tk.Tk()
app = Window(root)
root.wm_title("Letters recognition")
root.mainloop()