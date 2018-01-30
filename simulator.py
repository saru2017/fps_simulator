#!/usr/bin/env python
# -*- coding: utf-8 -*-


from frame import Frame
from player import Player
from game_controller import GameController
import tkinter as Tk

PLAYER_SIZE = 10
PLAYER_COLOR = 'red'
BULLET_SIZE = 10
BULLET_COLOR = 'red'

f = Frame()

def quit():
    f.quit()

def set_bullet(bullet):
    f.cvs.coords(
        bullet.id, bullet.x, bullet.y,
        bullet.x + BULLET_SIZE, bullet.y + BULLET_SIZE)

def simulator():
    player1 = Player.create(f, 0, 0)
    player2 = Player.create(f, 0, 0)
    gc = GameController(f, [player1, player2])
    print(player1.id, player2.id)

    def update():
        gc.update()
        print("player1: (%.1f, %.1f), player2: (%.1f, %.1f)" % (
            gc.players[0].x, gc.players[0].y,
            gc.players[1].x, gc.players[1].y))
        f.cvs.after(100, update)

    f.cvs.after(1000,quit)

    update()
    f.pack(fill=Tk.BOTH, expand=1)
    f.mainloop()
    return player1,player2

if __name__ == '__main__':
    print('--- simulator start ---')
    for i in range(0,10):
        result = simulator();
        print(result[0].damage,result[1].damage)
    print('--- simulator end ---')

