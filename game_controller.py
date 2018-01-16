import random


class GameController():
    def __init__(self, f, players):
        self.f = f
        self.players = players
        self.bullets = []

    def __set_object(self, object):
        self.f.cvs.coords(
            object.id, object.x, object.y,
            object.x + object.size, object.y + object.size)

    def player_move(self):
        for player in self.players:
            player.move()
            self.__set_object(player)

    def player_shot(self, index=-1):
        if index == -1:
            for player in self.players:
                player.shot(self.f, random.randint(-180, 180))
        elif index < len(self.players):
            bullet = self.players[index].shot(self.f, random.randint(-180, 180))
            self.bullets.append(bullet)

    def bullet_move(self):
        for bullet in self.bullets:
            bullet.move()
            self.__set_object(bullet)

    def update(self):
        self.player_move()
        self.player_shot(1)
        self.bullet_move()


if __name__ == '__main__':
    gc = GameController()
