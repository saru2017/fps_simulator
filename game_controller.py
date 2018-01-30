import random
import math
from const import (
    PLAYER_SIZE, PLAYER_VELOCITY, PLAYER_COLOR, WIDTH, HEIGHT, BULLET_SIZE, BULLET_DAMAGE)


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
            for player in self.players:
                bullet = player.shot(self.f, random.randint(-180, 180))
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
                    a = self.checkBalletPlayerCollision(b,p)
                    if a == True:
                        p.damage += BULLET_DAMAGE
                        del self.bullets[self.bullets.index(b)]
                        self.f.cvs.delete(b.id)

    def checkBalletPlayerCollision(self, b, p):
        for i in range(b.v):
            tmpx = b.x + (b.dx * i) / b.v
            tmpy = b.y + (b.dy * i) / b.v
            dist = math.sqrt(math.pow(p.x - tmpx,2)+math.pow(p.y - tmpy,2))
            if dist < (PLAYER_SIZE+BULLET_SIZE):
                return True
        return False

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
