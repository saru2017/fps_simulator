
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


def set_bullet(bullet):
    f.cvs.coords(
        bullet.id, bullet.x, bullet.y,
        bullet.x + BULLET_SIZE, bullet.y + BULLET_SIZE)


if __name__ == '__main__':
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

    update()
    f.pack(fill=Tk.BOTH, expand=1)
    f.mainloop()
