from game_controller import GameController
from utils import get_radian
import copy
import random
import math

from const import (WIDTH, HEIGHT)
from utils import get_radian
class Client_player():
    def __init__(self, frame, player, enemy, enemy_latency):
        self.player = player
        self.enemy = enemy
        self.enemy_late = copy.copy(enemy)
        self.enemy_latency = enemy_latency
        self.frame = frame
        self.event_queue = []
        self.bullets = []
    def connectClient(self, ctrl):
        self.enemy_controller = ctrl

    def __set_object(self, object):
        x1 = object.x
        y1 = object.y
        x2 = object.x + object.size
        y2 = object.y + object.size
        self.frame.cvs.coords(object.id, x1, y1, x2, y2)

    def __reserve_event(self, event_name, count, arg1=None):
        self.event_queue.append({
            'name': event_name,
            'count': count,
            'arg1': arg1
        })

    def move(self):
        self.player.move()
        self.__set_object(self.player)

    def shot(self, radian=None):
        if radian is None:
            radian = get_radian(
                self.player.x,
                self.player.y,
                self.enemy.x,
                self.enemy.y)
        bullet = self.player.shot(self.frame, radian)
        self.__set_object(bullet)
        self.bullets.append(bullet)

    def enemy_move(self):
        #相手の動きを取得
        #self.enemy.move()
        #self.__set_object(self.enemy)
        self.enemy_late = copy.copy(self.enemy)

    def enemy_shot(self):
        #相手の射撃を取得

        #相手のbulletsにあって自分のbulletsにないものを探査して、自分のbulletsにコピー
        new_bullets = []
        for b in self.enemy_controller.bullets:
            flag = False
            for b_ in self.bullets:
                if b.id == b_.id:
                    flag = True
                    break
            if  not flag:
                new_bullets.append(b)
                print(b)
        
        for nb in new_bullets:
            self.bullets.append(nb)
            self.__set_object(nb)
        
    def bullet_move(self):
        for bullet in self.bullets:
            bullet.move()
            self.__set_object(bullet)

    def reserve_move(self):
        self.__reserve_event('move', 0)

    def reserve_shot(self):
        radian = get_radian(
            self.player.x,
            self.player.y,
            self.enemy_late.x,
            self.enemy_late.y)
        self.__reserve_event('shot', 0, radian)

    def reserve_enemy_move(self):
        self.__reserve_event('enemy_move', self.enemy_latency)

    def reserve_enemy_shot(self):
        self.__reserve_event('enemy_shot', self.enemy_latency)

    def __do_event(self):
        # 実行
        done_event_indexes = []
        for i, event in enumerate(self.event_queue):
            if event['count'] <= 0:
                #print(event['name'])
                if event['arg1'] is None:
                    getattr(self, event['name'])()
                else:
                    getattr(self, event['name'])(event['arg1'])
                done_event_indexes.append(i)
        # 削除
        for index in sorted(done_event_indexes, reverse=True):
            del self.event_queue[index]
        # 進む
        for i in range(len(self.event_queue)):
            self.event_queue[i]['count'] -= 1

    def update(self):
        # 予約
        self.reserve_move()
        self.reserve_shot()
        self.reserve_enemy_move()
        self.reserve_enemy_shot()
        # 実行
        self.__do_event()
        self.bullet_move()
        self.checkCollision()
        self.checkBulletAlive()

    def checkCollision(self):
        for b in self.bullets[:]:
            if b.player_id != self.player.id:
                if self.checkBalletPlayerCollision(b, self.player):
                    self.player.damage += b.damage
                    del self.bullets[self.bullets.index(b)]
                    self.frame.cvs.delete(b.id)

    def checkBalletPlayerCollision(self, b, p):
        for i in range(b.v):
            tmpx = b.x + (b.dx * i) / b.v
            tmpy = b.y + (b.dy * i) / b.v
            dist = math.sqrt(math.pow(p.x - tmpx, 2) + math.pow(p.y - tmpy, 2))
            if dist < (p.size + b.size):
                return True
        return False

    def checkBulletAlive(self):
        for b in self.bullets:
            if (b.x < 0) or (b.x > WIDTH):
                del self.bullets[self.bullets.index(b)]
                self.frame.cvs.delete(b.id)
                continue
            if (b.y < 0) or (b.y > HEIGHT):
                del self.bullets[self.bullets.index(b)]
                self.frame.cvs.delete(b.id)
                continue

if __name__ == '__main__':
    import tkinter as Tk
    from frame import Frame
    from player import Player
    frame = Frame()
    player = Player.create(frame, 0, 0)
    enemy = Player.create(frame, 0, 0)
    ENEMY_LATENCY = 10
    client = Client(frame, player, enemy, ENEMY_LATENCY)

    def update():
        client.update()
        # print("player: (%.1f, %.1f), enemy: (%.1f, %.1f)" % (
        #     client.player.x, client.player.y,
        #     client.enemy.x, client.enemy.y))
        print("Damage1: (%.1d), Damage2: (%.1d)" % (
            client.players[0].damage, client.players[1].damage))
        frame.cvs.after(100, update)

    update()
    frame.pack(fill=Tk.BOTH, expand=1)
    frame.mainloop()
