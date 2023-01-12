import random

from pygame import Vector2
from pygame.time import get_ticks

from fustrum import Fustrum
from epidemie import EPIDEMIE

import core


class Body(object):
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.vitesse = Vector2()
        self.vMax = 2
        self.accMax = 10
        self.mass = 10
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.acc = Vector2()
        self.fustrum = Fustrum(EPIDEMIE["minimalDistanceContagion"], self)
        self.statut = random.randint(0,1)
        self.infectDate = 0

    def update(self):
        if self.acc.length() > self.accMax / self.mass:
            self.acc.scale_to_length(self.accMax / self.mass)

        self.vitesse = self.vitesse + self.acc

        if self.vitesse.length() > self.vMax:
            self.vitesse.scale_to_length(self.vMax)

        self.position = self.position + self.vitesse
        # core.Draw.line((255, 255, 255), self.position, self.position + self.acc * 100, 10)

        self.acc = Vector2()

        # incubationTime
        if self.statut == 1 and ((get_ticks()/1000)-self.infectDate > EPIDEMIE["incubationTime"]):
            self.statut = 2

        # check distance contagion
        if self.statut == 2:
            for x in self.fustrum.perceptionList:
                if x.statut == 0:
                    x.statut = 1
                    x.infectDate = get_ticks() / 1000

    def show(self):
        if self.statut == 0:
            core.Draw.circle((0, 255, 0), self.position, self.mass)
        if self.statut == 1:
            core.Draw.circle((0, 0, 255), self.position, self.mass)
        if self.statut == 2:
            core.Draw.circle((255, 0, 0), self.position, self.mass)

    def incubation(self):
        self.statut = 1

