from agent import Agent
from body import Body


class Decomposeur(Agent):
    def __init__(self):
        Agent.__init__(self,Body(2, 10, 100, 100, 100, 120, (96, 96, 96)))

    def update(self):
        Agent.update(self)