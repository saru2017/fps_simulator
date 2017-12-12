#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bullet
import player_const

class Player:
    def __init__(self, x, y):
        self.size = player_constPLAYER_SIZE
        self.vx=10
        self.vy=10

    # Playerの動き制御
    def moving(self):
        vx1 = self.ax+self.vx
        vy1 = self.ay+self.vy
        dx = (self.vx+vx1)/2
        dy = (self.vy+vy1)/2
        self.vx=vx1
        self.vy=vy1
        # 次の速度をランダムに
        self.ax = R.randint(-10,10) - self.vx/2
        self.ay = R.randint(-10,10) - self.vy/2
        # 壁に当たると反射する処理

    # 銃弾の発射
    def shot(self,radian):
        # bulletインスタンスの生成
        ## radianに沿ってbulletのインスタンスを生成する
        bullet = bullet(x,y,size,radian,v,damege)
        return bullet

if __name__ == '__main__':
    player = Player(250,250)
    while True:
        
        
        
    
