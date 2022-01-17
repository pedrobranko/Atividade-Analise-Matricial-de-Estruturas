import numpy as np


class TrussSolve:
    def __init__(self, builder):
        self.builder = builder
        self.FGlobal = []

    def getGlobalForces(self):
        for node in self.builder.nodeList:
            self.FGlobal.append(node.nodeList.fX)
            self.FGlobal.append(node.nodeList.fX)
