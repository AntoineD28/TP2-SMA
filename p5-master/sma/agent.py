import random

from pygame import Vector2

from body import Body


class Agent:
    def __init__(self, body):
        self.statut = random.randint(0,3)
        self.body = body
        self.uuid = random.randint(100000, 999999999)

    def update(self):
        target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
        while target.length() == 0:
            target = Vector2(random.randint(-1, 1), random.randint(-1, 1))
        self.body.acc += target
        self.body.update()

    def show(self):
        self.body.show()
