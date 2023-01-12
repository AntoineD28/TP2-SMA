import random

import math
from pygame.math import Vector2
import core
from body import Body

from superPred import SuperPred
from Carnivore import Carnivore
from Decomposeur import Decomposeur
from herbivore import Herbivore
from item import Item

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("agents", [])
    core.memory("superPred", [])
    core.memory("carnivore", [])
    core.memory("decomposeur", [])
    core.memory("herbivore", [])
    core.memory("items", [])

    for i in range(0,2):
        core.memory('agents').append(SuperPred())

    for i in range(0,2):
        core.memory('agents').append(Carnivore())

    for i in range(0,2):
        core.memory('agents').append(Decomposeur())

    for i in range(0,2):
        core.memory('agents').append(Herbivore())

    for i in range(0,25):
        core.memory('items').append(Item())


    print("Setup END-----------")


def computePerception(a):
    a.body.fustrum.perceptionList=[]
    for b in core.memory('agents'):
        if a.body.fustrum.inside(b.body) and a.uuid != b.uuid:
            a.body.fustrum.perceptionList.append(b.body)
    for b in core.memory('items'):
        if a.body.fustrum.inside(b):
            a.body.fustrum.perceptionList.append(b)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.update()

def run():
    core.cleanScreen()

    #Display
    for agent in core.memory("agents"):
        agent.show()
        if not isinstance(agent, Item):
            if math.floor(agent.body.reproduction) % agent.body.reproductionC == 0:
                core.memory("superPred").append(SuperPred())

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    for item in core.memory("items"):
        item.show()
     
core.main(setup, run)
