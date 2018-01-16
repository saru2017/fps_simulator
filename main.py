
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from frame import Frame
from player import Player
from game_controller import GameController
import tkinter as Tk

PLAYER_SIZE = 10
PLAYER_COLOR = 'red'


if __name__ == '__main__':
    f = Frame()
    player1 = Player(f.cvs.create_oval(0, 0, PLAYER_SIZE, PLAYER_SIZE, fill=PLAYER_COLOR, width=0), 0, 0)
    player2 = Player(f.cvs.create_oval(0, 0, PLAYER_SIZE, PLAYER_SIZE, fill=PLAYER_COLOR, width=0), 0, 0)
    gc = GameController([player1, player2])

    def move():
        def set(player):
            f.cvs.coords(player.id, player.x, player.y, player.x + PLAYER_SIZE, player.y + PLAYER_SIZE)
        gc.player_move()
        set(gc.players[0])
        set(gc.players[1])
        f.cvs.after(100, move)

    move()
    f.pack(fill=Tk.BOTH, expand=1)
    f.mainloop()
