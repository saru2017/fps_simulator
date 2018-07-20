import tkinter as Tk
from const import (WIDTH, HEIGHT)

BACKGROUND_COLOR = 'white'


class Frame(Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title("FPS Simulater")
        self.master.geometry("+20+20")
        self.cvs = Tk.Canvas(self, width=WIDTH, height=HEIGHT, relief=Tk.SUNKEN, borderwidth=2, bg=BACKGROUND_COLOR)
        self.cvs.pack(fill=Tk.BOTH, expand=1)
