import random

import math
import pygame
from pygame.math import Vector2
import core
from body import Body

from superPred import SuperPred
from Carnivore import Carnivore
from Decomposeur import Decomposeur
from herbivore import Herbivore
from item import Item

sp = 0
c = 0
h = 0
d = 0
def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [500, 500]

    core.memory("agents", [])
    core.memory("items", [])

    global sp
    global c
    global d
    global h

    for i in range(0,2):
        core.memory('agents').append(SuperPred())
        sp = sp + 1

    for i in range(0,2):
        core.memory('agents').append(Carnivore())
        c = c + 1

    for i in range(0,1):
        core.memory('agents').append(Decomposeur())
        d = d + 1

    for i in range(0,4):
        core.memory('agents').append(Herbivore())
        h = h +1

    for i in range(0,25):
        core.memory('items').append(Item())

    print("Setup END-----------")


def computePerception(a):
    a.body.fustrum.perceptionList=[]
    for b in core.memory('agents'):
        if a.body.fustrum.inside(b.body) and a.uuid != b.uuid:
            a.body.fustrum.perceptionList.append(b)
    for b in core.memory('items'):
        if a.body.fustrum.inside(b):
            a.body.fustrum.perceptionList.append(b)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.update()

def updateEnv():
    for a in core.memory("agents"):
        if isinstance(a, Herbivore):
            for c in core.memory('items'):
                if a.body.position.distance_to(c.position) <= a.body.mass:
                    core.memory("items").remove(c)
                    a.body.faim = 0
        if isinstance(a, Decomposeur):
            for c in core.memory("agents"):
                if a.body.position.distance_to(c.body.position) <= a.body.mass:
                    if c.body.isDead:
                        core.memory("agents").remove(c)
        if isinstance(a, SuperPred):
            for c in core.memory("agents"):
                if a.body.position.distance_to(c.body.position) <= a.body.mass:
                    if isinstance(c, Carnivore):
                        core.memory("agents").remove(c)
                        a.body.faim = 0
        if isinstance(a, Carnivore):
            for c in core.memory("agents"):
                if a.body.position.distance_to(c.body.position) <= a.body.mass:
                    if isinstance(c, Herbivore):
                        core.memory("agents").remove(c)
                        a.body.faim = 0
                        #c.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]),
                        #                     random.randint(0, core.WINDOW_SIZE[1]))
                        #c.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def run():
    core.cleanScreen()
    global sp
    global c
    global h


    #Display
    for agent in core.memory("agents"):
        agent.show()
        if not isinstance(agent, Item):
            if math.floor(agent.body.reproduction) % agent.body.reproductionC == 0:
                if isinstance(agent, SuperPred):
                    core.memory("agents").append(SuperPred())
                    sp = sp + 1
                elif isinstance(agent, Carnivore):
                    core.memory("agents").append(Carnivore())
                    c = c + 1
                elif isinstance(agent, Herbivore):
                    h = h + 1
                    core.memory("agents").append(Herbivore())
                elif isinstance(agent, Decomposeur):
                    core.memory("agents").append(Decomposeur())

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)

    for item in core.memory("items"):
        item.show()

    updateEnv()
     
core.main(setup, run)
