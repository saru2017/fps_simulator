#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bullet
from player_const import *
import random
import math
# for debug
import time

class Player:
    def __init__(self, x, y):
        self.size = PLAYER_SIZE
        self.x = x
        self.y = y

    # Playerの動き制御
    def move(self):
        radian = math.radians(random.randint(-180,180))
        vx = math.sin(radian) * PLAYER_VELOCITY 
        vy = math.cos(radian) * PLAYER_VELOCITY
        self.x += vx
        self.y += vy
        # 壁に当たると反射する処理
        if self.x < 0 :
            self.x = abs(self.x)
        elif self.x >  WIDTH:
            self.x = WIDTH - self.x % WIDTH
        if self.y < 0 :
            self.y = abs(self.y)
        elif self.y >  HEIGHT:
            self.y = HEIGHT - self.y % HEIGHT

    # 銃弾の発射
    def shot(self,radian):
        # bulletインスタンスの生成
        ## radianに沿ってbulletのインスタンスを生成する
        bullet = bullet(self.x,self.y,BULLET_SIZE,radian,BULLET_VELOCITY,BULLET_DAMAGE)
        return bullet

if __name__ == '__main__':
    player = Player(250,250)
    while True:
        player.move()
        print(player.x,player.y)
        time.sleep(1)
        
