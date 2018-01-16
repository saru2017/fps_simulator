import random


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


if __name__ == '__main__':
    gc = GameController()
