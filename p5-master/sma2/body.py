import random
import time
from math import floor

from pygame import Vector2
from pygame.time import get_ticks

from fustrum import Fustrum

import core


class Body(object):
    def __init__(self, _vMax, _accMax, _fat, _faim, _repro, _esp, _color):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.vitesse = Vector2()
        self.acc = Vector2()

        self.vMax = _vMax
        self.accMax = _accMax
        self.mass = 10

        self.faimC = _faim
        self.fatigueC = _fat
        self.reproductionC = _repro

        self.faim = 1
        self.fatigue = 1
        self.reproduction = 1

        self.dateNaiss = time.time()
        self.espVie = _esp
        self.color = _color
        self.colorTmp = _color
        self.isSleeping = False

        self.fustrum = Fustrum(30, self)

    def update(self):
        self.fatigue += 0.7
        self.faim += 0.1
        if time.time() - self.dateNaiss > self.espVie:
            self.color = (255, 255, 255)
        elif self.faim > self.faimC:
            self.color = (255, 255, 255)
        elif floor(self.fatigue) % self.fatigueC == 0:
            self.color = (220, 220, 220)
            self.isSleeping = not self.isSleeping
        else:
            if self.isSleeping == False:
                self.reproduction += 0.1
                self.color = self.colorTmp
                if self.acc.length() > self.accMax / self.mass:
                    self.acc.scale_to_length(self.accMax / self.mass)

                self.vitesse = self.vitesse + self.acc

                if self.vitesse.length() > self.vMax:
                    self.vitesse.scale_to_length(self.vMax)

                self.position = self.position + self.vitesse
                # core.Draw.line((255, 255, 255), self.position, self.position + self.acc * 100, 10)

                self.acc = Vector2()

    def show(self):
        core.Draw.circle(self.color, self.position, self.mass)
