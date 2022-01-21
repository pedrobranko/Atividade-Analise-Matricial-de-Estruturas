import numpy as np


class Material:
    def __init__(self, E, S):
        self.id = None
        self.E = E
        self.S = S

    def setId(self, id):
        self.id = id


class Node:
    def __init__(self, xNode, yNode, sup=None, fX=None, fY=None):
        self.id = None
        self.xNode = xNode
        self.yNode = yNode
        self.fX = fX if fX is not None else 0
        self.fY = fY if fY is not None else 0
        self.sup = sup if sup is not None else [0, 0]

    def setId(self, id):
        self.id = id

    def setForces(self, fX, fY):
        self.fX = fX
        self.fY = fY


class Truss:
    def __init__(self, nodes, I=None, S=None, E=None):
        self.id = None
        self.nodes = nodes
        self.I = I if I is not None else 0
        self.S = S
        self.E = E
        self.L = ((nodes[1].xNode - nodes[0].xNode) ** 2 + ((nodes[1].yNode - nodes[0].yNode) ** 2)) ** .5

        cos = (nodes[1].xNode - nodes[0].xNode) / self.L
        sen = (nodes[1].yNode - nodes[0].yNode) / self.L
        self.kLocal = np.matrix([[cos ** 2, cos * sen, -cos ** 2, -cos * sen],
                                 [cos * sen, sen ** 2, -cos * sen, -sen ** 2],
                                 [-cos ** 2, -cos * sen, cos ** 2, cos * sen],
                                 [-cos * sen, -sen ** 2, cos * sen, sen ** 2]])
        self.kLocal = self.kLocal * (self.E * self.S / self.L)
        self.globalPositionElem = []
        self.kGlobalElem = []

    def setId(self, id):
        self.id = id

    def setElementGlobalParameters(self, nNodes):
        BMatrixI = np.zeros([4, 2 * nNodes])
        j1 = 2 * self.nodes[0].id
        j2 = 2 * self.nodes[0].id + 1
        k1 = 2 * self.nodes[1].id
        k2 = 2 * self.nodes[1].id + 1
        BMatrixI[0][j1] = 1
        BMatrixI[1][j2] = 1
        BMatrixI[2][k1] = 1
        BMatrixI[3][k2] = 1
        self.kGlobalElem = (np.matmul(np.matmul(BMatrixI.T, self.kLocal), BMatrixI))
        self.globalPositionElem = BMatrixI
