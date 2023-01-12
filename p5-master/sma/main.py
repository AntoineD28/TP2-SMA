import random

import math
from pygame.math import Vector2
import core
from body import Body
from agent import Agent

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("agents", [])
    core.memory("item", [])

    for i in range(0,20):
        core.memory('agents').append(Agent(Body()))

    idAgent = 0

    print("Setup END-----------")


def computePerception(agent):
    agent.body.fustrum.perceptionList=[]
    for b in core.memory('agents'):
        if agent.uuid!=b.uuid:
            if agent.body.fustrum.inside(b.body):
                agent.body.fustrum.perceptionList.append(b.body)


def computeDecision(agent):
    agent.update()


def applyDecision(agent):
    agent.body.update()

def putOneInfecte():
    idMin=0
    minDist=math.inf
    for a in core.memory("agents"):
        if (a.body.position.distance_to(core.getMouseLeftClick()) <= minDist):
            idMin=a.uuid
            minDist=a.body.position.distance_to(core.getMouseLeftClick())
    for a in core.memory("agents"):
        if(a.uuid==idMin):
            print(a.uuid)
            a.body.incubation()

def run():
    core.cleanScreen()

    if core.getMouseLeftClick():
        putOneInfecte()

    #Display
    for agent in core.memory("agents"):
        agent.show()
        agent.update()

    for item in core.memory("item"):
        item.show()

    for agent in core.memory("agents"):
        computePerception(agent)

    for agent in core.memory("agents"):
        computeDecision(agent)

    for agent in core.memory("agents"):
        applyDecision(agent)
    
    
    
    
     
core.main(setup, run)
