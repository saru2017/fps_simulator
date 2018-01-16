#!/usr/bin/env python
# -*- coding: utf-8 -*-

from object import Object
from bullet import Bullet
from const import (
    PLAYER_SIZE, PLAYER_VELOCITY, PLAYER_COLOR, WIDTH, HEIGHT)
import random
import math
# for debug
import time


class Player(Object):
    def __init__(self, id, x, y):
        super().__init__(id, x, y, PLAYER_SIZE, PLAYER_COLOR)

    @classmethod
    def create(cls, f, x, y):
        return cls(f.cvs.create_oval(
            x, y, PLAYER_SIZE, PLAYER_SIZE,
            fill=PLAYER_COLOR, width=0), x, y)

    # Playerの動き制御
    def move(self):
        radian = math.radians(random.randint(-180, 180))
        vx = math.sin(radian) * PLAYER_VELOCITY
        vy = math.cos(radian) * PLAYER_VELOCITY
        self.x += vx
        self.y += vy
        # 壁に当たると反射する処理
        if self.x < 0:
            self.x = abs(self.x)
        elif self.x > WIDTH:
            self.x = WIDTH - self.x % WIDTH
        if self.y < 0:
            self.y = abs(self.y)
        elif self.y > HEIGHT:
            self.y = HEIGHT - self.y % HEIGHT

    # 銃弾の発射
    def shot(self, f, radian):
        # bulletインスタンスの生成
        # radianに沿ってbulletのインスタンスを生成する
        bullet = Bullet.create(f, self.id, self.x, self.y, radian)
        return bullet

if __name__ == '__main__':
    player = Player(250, 250)
    while True:
        player.move()
        print(player.x, player.y)
        time.sleep(1)
