import random

from utils import get_radian


class Client():
    def __init__(self, frame, player, enemy, enemy_latency):
        self.frame = frame
        self.player = player
        self.enemy = enemy
        self.enemy_latency = enemy_latency

        self.bullets = []
        self.event_queue = []

    def __set_object(self, object):
        x1 = object.x
        y1 = object.y
        x2 = object.x + object.size
        y2 = object.y + object.size
        self.frame.cvs.coords(object.id, x1, y1, x2, y2)

    def __reserve_event(self, event_name, count):
        self.event_queue.append({
            'name': event_name,
            'count': count
        })

    def move(self):
        self.player.move()
        self.__set_object(self.player)

    def shot(self):
        radian = get_radian(
            self.player.x,
            self.player.y,
            self.enemy.x,
            self.enemy.y)
        bullet = self.player.shot(self.frame, radian)
        self.__set_object(bullet)
        self.bullets.append(bullet)

    def enemy_move(self):
        self.enemy.move()
        self.__set_object(self.enemy)

    def enemy_shot(self):
        bullet = self.enemy.shot(self.frame, random.randint(-180, 180))
        self.__set_object(bullet)
        self.bullets.append(bullet)

    def bullet_move(self):
        for bullet in self.bullets:
            bullet.move()
            self.__set_object(bullet)

    def reserve_move(self):
        self.__reserve_event('move', 0)

    def reserve_shot(self):
        self.__reserve_event('shot', 0)

    def reserve_enemy_move(self):
        self.__reserve_event('enemy_move', self.enemy_latency)

    def reserve_enemy_shot(self):
        self.__reserve_event('enemy_shot', self.enemy_latency)

    def __do_event(self):
        # 実行
        done_event_indexes = []
        for i, event in enumerate(self.event_queue):
            if event['count'] <= 0:
                getattr(self, event['name'])()
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


if __name__ == '__main__':
    import tkinter as Tk
    from frame import Frame
    from player import Player
    frame = Frame()
    player = Player.create(frame, 0, 0)
    enemy = Player.create(frame, 0, 0)
    ENEMY_LATENCY = 3
    client = Client(frame, player, enemy, ENEMY_LATENCY)

    def update():
        client.update()
        # print("player: (%.1f, %.1f), enemy: (%.1f, %.1f)" % (
        #     client.player.x, client.player.y,
        #     client.enemy.x, client.enemy.y))
        print(client.event_queue)
        frame.cvs.after(100, update)

    update()
    frame.pack(fill=Tk.BOTH, expand=1)
    frame.mainloop()
