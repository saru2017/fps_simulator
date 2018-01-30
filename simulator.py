#!/usr/bin/env python
# -*- coding: utf-8 -*-


from frame import Frame
from player import Player
from game_controller import GameController
from client import Client
import tkinter as Tk


def simulator(RUN_COUNT=100):
    f = Frame()
    FRAME_TIME = 10

    player1 = Player.create(f, 0, 0)
    player2 = Player.create(f, 0, 0)
    gc = GameController(f, [player1, player2])
    print(player1.id, player2.id)

    def update():
        gc.update()
        print("player1: (%.1f, %.1f), player2: (%.1f, %.1f)" % (
            gc.players[0].x, gc.players[0].y,
            gc.players[1].x, gc.players[1].y))
        f.cvs.after(FRAME_TIME, update)

    f.cvs.after(RUN_COUNT * FRAME_TIME, f.quit)

    update()
    f.pack(fill=Tk.BOTH, expand=1)
    f.mainloop()
    return player1, player2


def simulator2(RUN_COUNT=100):
    f = Frame()
    FRAME_TIME = 10

    player1 = Player.create(f, 0, 0)
    player2 = Player.create(f, 0, 0)
    gc = Client(f, player1, player2, 5)
    print(player1.id, player2.id)

    def update():
        gc.update()
        print("player1: (%.1f, %.1f), player2: (%.1f, %.1f)" % (
            gc.players[0].x, gc.players[0].y,
            gc.players[1].x, gc.players[1].y))
        f.cvs.after(FRAME_TIME, update)

    f.cvs.after(RUN_COUNT * FRAME_TIME, f.quit)

    update()
    f.pack(fill=Tk.BOTH, expand=1)
    f.mainloop()
    return player1, player2

if __name__ == '__main__':
    print('--- simulator start ---')
    results = []
    for i in range(0, 10):
        result = simulator()
        results.append((result[0].damage, result[1].damage))
        print(result[0].damage, result[1].damage)
    print('--- simulator end ---')
    print('--- simulator start ---')
    results2 = []
    for i in range(0, 10):
        result = simulator2()
        results2.append((result[0].damage, result[1].damage))
        print(result[0].damage, result[1].damage)
    print('--- simulator end ---')
    print(results)
    print(results2)
