from const import WIDTH, HEIGHT
# from player import Player


class GameController():
    players = []
    bullets = []

    def __init__(self, players):
        self.players = players

    def player_move(self):
        for player in self.players:
            player.move()

    def player_shoot(self, index=-1):
        if index == -1:
            for player in self.players:
                player.shoot()
        elif index < len(self.players):
            self.players[index].shoot

    def bullet_move(self):
        for bullet in self.bullets:
            bullet.move()

    def update(self):
        self.player_move()
        self.player_shoot()
        self.bullet_move()


if __name__ == '__main__':
    gc = GameController()
    print(WIDTH, HEIGHT)
