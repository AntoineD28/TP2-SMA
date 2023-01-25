from agent import Agent
from body import Body

from item import Item
from Decomposeur import Decomposeur
import superPred

class Herbivore(Agent):
    def __init__(self):
        Agent.__init__(self, Body(3, 50, 25, 50, 150, 70, (128, 128, 0), 4))
        self.coefObs = 100
        self.coefItem = .01

    def filtrePerception(self):
        manger = []
        danger = []
        for i in self.body.fustrum.perceptionList:
            if isinstance(i, Item):
                i.dist = self.body.position.distance_to(i.position)
            else:
                i.dist = self.body.position.distance_to(i.body.position)
            if isinstance(i, Item):
                manger.append(i)
            else:
                if not isinstance(i, Decomposeur) and not isinstance(i, Herbivore) and not isinstance(i, superPred.SuperPred):
                    danger.append(i.body)

        manger.sort(key=lambda x: x.dist, reverse=False)
        danger.sort(key=lambda x: x.dist, reverse=False)

        return danger, manger

    def update(self):
        Agent.update(self)

        danger, manqer = self.filtrePerception()

        if len(manqer) > 0:
            target = manqer[0].position - self.body.position
            target.scale_to_length(target.length() * self.coefItem)
            self.body.acc = self.body.acc + target

        if len(danger) > 0:
            print("herbivore danger")
            target = self.body.position - danger[0].position
            target.scale_to_length(1 / target.length() ** 2)
            target.scale_to_length(target.length() * (self.coefObs + self.body.mass))
            self.body.acc = self.body.acc + target