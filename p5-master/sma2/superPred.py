from agent import Agent
from body import Body

from item import Item
from Decomposeur import Decomposeur

class SuperPred(Agent):
    def __init__(self):
        Agent.__init__(self, Body(3, 12, 100, 100, 100, 120, (255, 0, 0)))

    def filtrePerception(self):
        manger = []
        for i in self.body.fustrum.perceptionList:
            i.dist = self.body.position.distance_to(i.position)
            if not isinstance(i, Item) and not isinstance(i, Decomposeur):
                manger.append(i)

        manger.sort(key=lambda x: x.dist, reverse=False)

        return manger

    def update(self):
        manqer=self.filtrePerception()

        if len(manqer)>0:
            target = manqer[0].position - self.body.position
            target.scale_to_length(target.length())
            self.body.acc = self.body.acc + target

        Agent.update(self)
