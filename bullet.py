from object import Object
from const import (
    BULLET_SIZE, BULLET_VELOCITY, BULLET_DAMAGE, BULLET_COLOR)
import math


class Bullet(Object):
    def __init__(self, id, x, y, radian, size=BULLET_SIZE, v=BULLET_VELOCITY, damage=BULLET_DAMAGE, color=BULLET_COLOR):
        super().__init__(id, x, y, size, color)
        self.radian = radian

        self.v = v
        self.damage = damage
        self.dx = math.cos(radian) * v
        self.dy = math.sin(radian) * v

    @classmethod
    def create(cls, f, x, y, radian):
        return cls(f.cvs.create_oval(
            x, y, BULLET_SIZE, BULLET_SIZE,
            fill=BULLET_COLOR, width=0), x, y, radian)

    def move(self):
        self.x += self.dx
        self.y += self.dy

if __name__ == '__main__':
    print("sucsess")
