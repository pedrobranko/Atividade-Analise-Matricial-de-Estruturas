import numpy as np


class Node:
    def __init__(self, xNode, yNode, sup=None):
        self.id = None
        self.xNode = xNode
        self.yNode = yNode
        self.sup = sup if sup is not None else [0, 0]

    def setId(self, id):
        self.id = id


class LinStructure:
    def __init__(self, nodes, I=None, A=None, E=None):
        self.id = None
        self.nodes = nodes
        self.I = I
        self.A = A
        self.E = E
        self.L = ((nodes[1].xNode - nodes[0].xNode) ** 2 + ((nodes[1].yNode - nodes[0].yNode) ** 2)) ** .5

        cos = (nodes[1].xNode - nodes[0].xNode) / self.L
        sen = (nodes[1].yNode - nodes[0].yNode) / self.L
        self.kLocal = np.matrix([[cos ** 2, cos * sen, -cos ** 2, -cos * sen],
                                 [cos * sen, sen ** 2, -cos * sen, -sen ** 2],
                                 [-cos ** 2, -cos * sen, cos ** 2, cos * sen],
                                 [-cos * sen, -sen ** 2, cos * sen, sen ** 2]])

    def setId(self, id):
        self.id = id
