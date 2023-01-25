from agent import Agent
from body import Body

from item import Item

class Decomposeur(Agent):
    def __init__(self):
        Agent.__init__(self, Body(2, 10, 100, 100, 200, 100, (96, 96, 96), 3))
        self.coefDead = 0.01
    def filtrePerception(self):
        manger = []
        for i in self.body.fustrum.perceptionList:
            if isinstance(i, Item):
                i.dist = self.body.position.distance_to(i.position)
            else:
                i.dist = self.body.position.distance_to(i.body.position)
            if not isinstance(i, Item):
                if i.body.isDead:
                    manger.append(i.body)

        manger.sort(key=lambda x: x.dist, reverse=False)

        return manger

    def update(self):
        Agent.update(self)

        manqer = self.filtrePerception()

        if len(manqer) > 0:
            target = manqer[0].position - self.body.position
            target.scale_to_length(target.length() * self.coefDead)
            self.body.acc = self.body.acc + target