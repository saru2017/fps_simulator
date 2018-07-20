#!/usr/bin/env python
# -*- coding: utf-8 -*-


from frame import Frame
from player import Player
from game_controller import GameController
from client import Client
from client_player import Client_player
import tkinter as Tk
import random
from const import (WIDTH, HEIGHT)
import csv

p1_latency = 0
p2_latency = 7


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

def simulator3(RUN_COUNT=100):
    #f = Frame()
    f1 = Frame()
    f2 = Frame()
    FRAME_TIME = 10

    #player1 = Player.create(f, random.randrange(WIDTH), random.randrange(HEIGHT))
    #player2 = Player.create(f, random.randrange(WIDTH), random.randrange(HEIGHT))
    player1 = Player.create(f1, random.randrange(WIDTH), random.randrange(HEIGHT))
    player2 = Player.create(f1, random.randrange(WIDTH), random.randrange(HEIGHT))

    #player1.id = 1
    #player2.id = 2

    #cli1 = Client_player(f, player1, player2, 0)
    #cli2 = Client_player(f, player2, player1, 50)

    cli1 = Client_player(f1, player1, player2, p1_latency)
    cli2 = Client_player(f1, player2, player1, p2_latency)

    cli1.connectClient(cli2)
    cli2.connectClient(cli1)

    #gc = Client(f, player1, player2, 5)
    #print('f1: {}, f2:{}'.format(f1, f2))
    print(player1.id, player2.id)

    def update():
        cli1.update()
        cli2.update()
        """
        print("player1: (%.1f, %.1f), player2: (%.1f, %.1f)" % (
            gc.players[0].x, gc.players[0].y,
            gc.players[1].x, gc.players[1].y))
        """
        f1.cvs.after(FRAME_TIME, update)
        #f2.cvs.after(FRAME_TIME, update)
        #f.cvs.after(FRAME_TIME, update)

    f1.cvs.after(RUN_COUNT * FRAME_TIME, f1.quit)
    #f2.cvs.after(RUN_COUNT * FRAME_TIME, f2.quit)
    #f.cvs.after(RUN_COUNT * FRAME_TIME, f.quit)

    update()
    f1.pack(fill=Tk.BOTH, expand=1)
    #f2.pack(fill=Tk.BOTH, expand=1)
    f1.mainloop()
    #f2.mainloop()
    #f.pack(fill=Tk.BOTH, expand=1)
    #f.mainloop()
    return player1, player2

if __name__ == '__main__':
    """
    print('--- simulator start ---')
    results = []
    for i in range(0, 10):
        result = simulator()
        results.append((result[0].damage, result[1].damage))
        print(result[0].damage, result[1].damage)
    print('--- simulator end ---')
    print('--- simulator start ---')
    """
    results2 = []
    #for i in range(0, 100):
    result = simulator3()
    results2.append((result[0].damage, result[1].damage))
    print(result[0].damage, result[1].damage)
    file_name = "Result_Latency#P1-{0}_P2-{1}.csv".format(p1_latency, p2_latency)
    with open(file_name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([result[0].damage, result[1].damage])
    print('--- simulator end ---')
    #print(results)
    print(results2)
