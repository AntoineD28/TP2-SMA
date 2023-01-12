from agent import Agent
from body import Body

from item import Item
from Decomposeur import Decomposeur

class Herbivore(Agent):
    def __init__(self):
        Agent.__init__(self, Body(1, 10, 100, 100, 100, 120, (128, 128, 0)))

    def filtrePerception(self):
        manger = []
        danger = []
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if isinstance(i, Item):
                manger.append(i)
            else:
                if not isinstance(i, Decomposeur):
                    danger.append(i)

        manger.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)

        return danger, manger

    def update(self):
        Agent.update(self)

        danger, manqer = self.filtrePerception()

        if len(manqer) > 0:
            target = manqer[0].position - self.body.position
            target.scale_to_length(target.length())
            self.body.acc = self.body.acc + target

        if len(danger) > 0:
            target = self.body.position - danger[0].position
            target.scale_to_length(1 / target.length() ** 2)
            target.scale_to_length(target.length() * self.body.mass)
            self.body.acc = self.body.acc + target