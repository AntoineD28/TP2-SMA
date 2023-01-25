from agent import Agent
from body import Body

from item import Item
from Decomposeur import Decomposeur
from herbivore import Herbivore


class SuperPred(Agent):
    def __init__(self):
        Agent.__init__(self, Body(3, 12, 30, 50, 150, 70, (255, 0, 0), 1))
        self.coefCarnivore = .01
    def filtrePerception(self):
        manger = []
        for i in self.body.fustrum.perceptionList:
            if isinstance(i, Item):
                i.dist = self.body.position.distance_to(i.position)
            else:
                i.dist = self.body.position.distance_to(i.body.position)
            if not isinstance(i, Item):
                if not i.body.isDead and not isinstance(i, Herbivore) and not isinstance(i, Decomposeur):
                    manger.append(i.body)

        manger.sort(key=lambda x: x.dist, reverse=False)

        #for i in manger:
            #print('SuperPred : ', isinstance(i, SuperPred))
            #print('SuperPred : ', isinstance(i, Herbivore))
            #print('SuperPred : ', isinstance(i, Carnivore))

        return manger

    def update(self):
        manqer=self.filtrePerception()

        if len(manqer)>0:
            target = manqer[0].position - self.body.position
            target.scale_to_length(target.length() * self.coefCarnivore)
            self.body.acc = self.body.acc + target

        Agent.update(self)
