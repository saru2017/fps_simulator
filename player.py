#!/usr/bin/env python
# -*- coding: utf-8 -*-

from object import Object
from bullet import Bullet
from const import (
    PLAYER_SIZE, PLAYER_VELOCITY, PLAYER_COLORS, WIDTH, HEIGHT)
import random
import math
# for debug
import time


class Player(Object):
    count = 0

    def __init__(self, id, x, y):
        color_index = (id - 1) % len(PLAYER_COLORS)
        super().__init__(id, x, y, PLAYER_SIZE, PLAYER_COLORS[color_index])
        self.radian = math.radians(random.randint(-180, 180))
        self.count = 0
        self.vx = math.sin(self.radian) * PLAYER_VELOCITY
        self.vy = math.cos(self.radian) * PLAYER_VELOCITY
        self.damage = 0

    @classmethod
    def create(cls, f, x, y, visible = True):
        color_index = cls.count % len(PLAYER_COLORS)
        cls.count += 1
        if visible:
            return cls(f.cvs.create_oval(
                x, y, PLAYER_SIZE, PLAYER_SIZE,
                fill=PLAYER_COLORS[color_index], width=0), x, y)
        else:
            return cls(-1, x, y)

    # Player の角度変更
    def set_radian(self, radian):
        self.radian = radian
        self.vx = math.sin(self.radian) * PLAYER_VELOCITY
        self.vy = math.cos(self.radian) * PLAYER_VELOCITY

    # Playerの動き制御
    def move(self):
        if self.count > 10:
            self.radian = math.radians(random.randint(-180, 180))
            self.vx = math.sin(self.radian) * PLAYER_VELOCITY
            self.vy = math.cos(self.radian) * PLAYER_VELOCITY
            self.count = 0
        else:
            self.count += 1

        # 壁に当たると反射する処理
        if self.x < 0:
            self.vx *= -1
        elif self.x > WIDTH:
            self.vx *= -1
        if self.y < 0:
            self.vy *= -1
        elif self.y > HEIGHT:
            self.vy *= -1

        self.x += self.vx
        self.y += self.vy

    # 銃弾の発射
    def shot(self, f, radian, visible = True):
        # bulletインスタンスの生成
        # radianに沿ってbulletのインスタンスを生成する
        bullet = Bullet.create(f, self.id, self.x, self.y, radian, visible = visible)
        return bullet

if __name__ == '__main__':
    player = Player(250, 250)
    while True:
        player.move()
        print(player.x, player.y)
        time.sleep(1)
