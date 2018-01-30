import random
import math

from const import (WIDTH, HEIGHT, BULLET_SIZE, BULLET_DAMAGE)
from utils import get_radian


class GameController():
    def __init__(self, f, players):
        self.f = f
        self.players = players
        self.bullets = []

    def __set_object(self, object):
        x1 = object.x
        y1 = object.y
        x2 = object.x + object.size
        y2 = object.y + object.size
        self.f.cvs.coords(object.id, x1, y1, x2, y2)

    def player_move(self):
        for player in self.players:
            player.move()
            self.__set_object(player)

    def player_shot(self, index=-1):
        if index == -1:
            for i, player in enumerate(self.players):
                enemy_index = (i + 1) % len(self.players)
                radian = get_radian(
                    player.x,
                    player.y,
                    self.players[enemy_index].x,
                    self.players[enemy_index].y)
                bullet = player.shot(self.f, radian)
                self.__set_object(bullet)
                self.bullets.append(bullet)
        elif index < len(self.players):
            bullet = self.players[index].shot(self.f, random.randint(-180, 180))
            self.bullets.append(bullet)
            self.__set_object(bullet)

    def bullet_move(self):
        for bullet in self.bullets:
            bullet.move()
            self.__set_object(bullet)

    def update(self):
        self.player_move()
        self.player_shot()
        self.bullet_move()
        self.checkCollision()
        self.checkBulletAlive()

    def checkCollision(self):
        for p in self.players[:]:
            for b in self.bullets[:]:
                if b.player_id != p.id:
                    dist = math.sqrt(math.pow(p.x - b.x, 2) + math.pow(p.y - b.y, 2))
                    if dist < (p.size + b.size):
                        p.damage += b.damage
                        del self.bullets[self.bullets.index(b)]
                        self.f.cvs.delete(b.id)

    def checkBulletAlive(self):
        for b in self.bullets:
            if (b.x < 0) or (b.x > WIDTH):
                del self.bullets[self.bullets.index(b)]
                self.f.cvs.delete(b.id)
                continue
            if (b.y < 0) or (b.y > HEIGHT):
                del self.bullets[self.bullets.index(b)]
                self.f.cvs.delete(b.id)
                continue


if __name__ == '__main__':
    gc = GameController()
