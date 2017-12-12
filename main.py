#!/usr/bin/env python

import sys
import tkinter

tk = tkinter.Tk()
tk.title("FPS simulator")
tk.geometry("320x320")

canvas = tkinter.Canvas(tk, width = 320, height = 320, bg="#fff")
canvas.place(x = 0, y = 0)

# Draw Circle on Canvas
dia = 10
centerX, centerY = 160, 160
id = canvas.create_oval(centerX - dia/2, centerY - dia/2,
                        centerX + dia/2, centerY + dia/2,
                        fill="#0000ff")



tk.mainloop()
