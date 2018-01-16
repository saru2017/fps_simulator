#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bullet import Bullet
from player_const import *
import random
import math
# for debug
import time


class Player:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.size = PLAYER_SIZE
        self.radian = math.radians(random.randint(-180, 180))
        self.count = 0
        self.vx = math.sin(self.radian) * PLAYER_VELOCITY
        self.vy = math.cos(self.radian) * PLAYER_VELOCITY

    # Player の角度変更
    def setRadian(newRadian):
        self.radian = newRadian
        self.vx = math.sin(self.radian) * PLAYER_VELOCITY
        self.vy = math.cos(self.radian) * PLAYER_VELOCITY

    # Playerの動き制御
    def move(self):
        if self.count > 10 :
            self.radian = math.radians(random.randint(-180, 180))
            self.vx = math.sin(self.radian) * PLAYER_VELOCITY
            self.vy = math.cos(self.radian) * PLAYER_VELOCITY
            self.count = 0
        else :
            self.count += 1

        print(self.count)
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
    def shot(self, radian):
        # bulletインスタンスの生成
        # radianに沿ってbulletのインスタンスを生成する
        bullet = Bullet(self.x, self.y, BULLET_SIZE, radian, BULLET_VELOCITY, BULLET_DAMAGE)
        return bullet

if __name__ == '__main__':
    player = Player(250, 250)
    while True:
        player.move()
        print(player.x, player.y)
        time.sleep(1)
