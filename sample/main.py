#!/usr/bin/env python
# -*- coding: utf-8 -*-


import tkinter as Tk
import random as R
     
PLAYER_SIZE = 10
PLAYER_COLOR = 'red'
BACKGROUND_COLOR = 'white'
     
class Player:
    canvas = None
    def __init__(self, x, y):
        self.id = Player.canvas.create_oval(x-PLAYER_SIZE, y-PLAYER_SIZE,x+PLAYER_SIZE, y+PLAYER_SIZE,fill=PLAYER_COLOR, width=0)
        self.vx=0
        self.vy=0
        self.ax = R.randint(-10,10)
        self.ay = R.randint(-10,10)

    # Playerの動き制御
    def moving(self):
        vx1=self.ax+self.vx
        vy1=self.ay+self.vy
        dx = (self.vx+vx1)/2
        dy = (self.vy+vy1)/2
        Player.canvas.move(self.id, dx, dy)
        self.vx=vx1
        self.vy=vy1
        self.ax = R.randint(-10,10) - self.vx/2
        self.ay = R.randint(-10,10) - self.vy/2
        print(self.ax,self.ay)
            
class Frame (Tk.Frame):
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title("FPS Simulater")
        self.master.geometry("+20+20")
        self.cvs = Tk.Canvas(self, width=500, height=500, relief=Tk.SUNKEN, borderwidth=2, bg=BACKGROUND_COLOR)
        self.cvs.pack(fill=Tk.BOTH, expand=1)
        Player.canvas=self.cvs
        x=R.randint(50, 450)
        y=R.randint(50, 450)
        self.playerA = Player(x,y)
        x=R.randint(50, 450)
        y=R.randint(50, 450)
        self.playerB = Player(x,y)
        self.move_player()
        
    def move_player(self):
        self.playerA.moving()
        self.playerB.moving()
        self.cvs.after(100, self.move_player)
     
     ##-----------------------------------------------------
if __name__ == '__main__':
    f = Frame()
    f.pack(fill=Tk.BOTH, expand=1)
    f.mainloop()
