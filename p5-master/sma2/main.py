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
    core.memory("item", [])

    for i in range(0,2):
        core.memory('superPred').append(SuperPred())

    for i in range(0,2):
        core.memory('carnivore').append(Carnivore())

    for i in range(0,2):
        core.memory('decomposeur').append(Decomposeur())

    for i in range(0,2):
        core.memory('herbivore').append(Herbivore())

    for i in range(0,25):
        core.memory('item').append(Item())


    print("Setup END-----------")


def computePerception(a):
    a.body.fustrum.perceptionList=[]
    for b in core.memory('carnivore'):
        if a.uuid != b.uuid:
            if a.body.fustrum.inside(b.body):
                a.body.fustrum.perceptionList.append(b.body)
    for b in core.memory('decomposeur'):
        if a.body.fustrum.inside(b):
            a.body.fustrum.perceptionList.append(b)

    for b in core.memory('herbivore'):
        if a.body.fustrum.inside(b):
            a.body.fustrum.perceptionList.append(b)

    for b in core.memory('superPred'):
        if a.body.fustrum.inside(b):
            a.body.fustrum.perceptionList.append(b)

    for b in core.memory('item'):
        if a.body.fustrum.inside(b):
            a.body.fustrum.perceptionList.append(b)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.update()

def run():
    core.cleanScreen()

    #Display
    for agent in core.memory("superPred"):
        agent.show()
        if math.floor(agent.body.reproduction) % agent.body.reproductionC == 0:
            core.memory("superPred").append(SuperPred())

    for agent in core.memory("carnivore"):
        agent.show()

    for agent in core.memory("decomposeur"):
        agent.show()
        #agent.update()

    for agent in core.memory("herbivore"):
        agent.show()

    for agent in core.memory("item"):
        agent.show()

    for agent in core.memory("superPred"):
        computePerception(agent)

    ## superPred
    for agent in core.memory("superPred"):
        computeDecision(agent)

    for agent in core.memory("superPred"):
        applyDecision(agent)

    ## Carnivore
    for agent in core.memory('carnivore'):
        computePerception(agent)

    for agent in core.memory('carnivore'):
        computeDecision(agent)

    for agent in core.memory('carnivore'):
        applyDecision(agent)

    ## Decomposeur
    for agent in core.memory('decomposeur'):
        computePerception(agent)

    for agent in core.memory('decomposeur'):
        computeDecision(agent)

    for agent in core.memory('decomposeur'):
        applyDecision(agent)

    ## Herbivore
    for agent in core.memory('herbivore'):
        computePerception(agent)

    for agent in core.memory('herbivore'):
        computeDecision(agent)

    for agent in core.memory('herbivore'):
        applyDecision(agent)
     
core.main(setup, run)
