from object import Object
from const import (
    BULLET_SIZE, BULLET_VELOCITY, BULLET_DAMAGE, BULLET_COLORS)
import math


class Bullet(Object):
    def __init__(self, id, x, y, radian, player_id=-1, size=BULLET_SIZE, v=BULLET_VELOCITY, damage=BULLET_DAMAGE, color=BULLET_COLORS[0]):
        super().__init__(id, x, y, size, color)
        self.player_id = player_id
        self.radian = radian

        self.v = v
        self.damage = damage
        self.dx = math.cos(radian) * v
        self.dy = math.sin(radian) * v

    @classmethod
    def create(cls, f, player_id, x, y, radian, visible = True):
        bullet_index = (player_id - 1) % len(BULLET_COLORS)
        # print(player_id, x, y, radian)
        if visible:
            return cls(f.cvs.create_oval(
                x, y, BULLET_SIZE, BULLET_SIZE,
                fill=BULLET_COLORS[bullet_index],
                width=0), x, y, radian, player_id=player_id)
        else:
            return cls(-1, x, y, radian, player_id=player_id)

    def move(self):
        self.x += self.dx
        self.y += self.dy
