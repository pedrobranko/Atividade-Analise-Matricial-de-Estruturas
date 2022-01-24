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
        self.J = [2 * self.nodes[0].id, 2 * self.nodes[0].id + 1]
        self.K = [2 * self.nodes[1].id, 2 * self.nodes[1].id + 1]
        self.L = ((nodes[1].xNode - nodes[0].xNode) ** 2 + ((nodes[1].yNode - nodes[0].yNode) ** 2)) ** .5
        rElem = np.array([[1, 0, -1, 0], [0, 0, 0, 0], [-1, 0, 1, 0], [0, 0, 0, 0]])
        self.rElem = np.multiply(rElem, (self.E * self.S / self.L))
        self.cos = (nodes[1].xNode - nodes[0].xNode) / self.L
        self.sen = (nodes[1].yNode - nodes[0].yNode) / self.L
        self.bElem = np.array([[self.cos, self.sen, 0, 0], [-self.sen, self.cos, 0, 0], [0, 0, self.cos, self.sen], [0, 0, -self.sen, self.cos]])
        self.RElem = np.matmul(np.matmul(self.bElem.transpose(), self.rElem), self.bElem)
        self.globalPositionElem = []
        self.RGlobalElem = []

    def setId(self, id):
        self.id = id

    def setElementGlobalParameters(self, nNodes):
        BMatrixI = np.zeros([4, 2 * nNodes])
        BMatrixI[0][self.J[0]] = 1
        BMatrixI[1][self.J[1]] = 1
        BMatrixI[2][self.K[0]] = 1
        BMatrixI[3][self.K[1]] = 1
        self.RGlobalElem = (np.matmul(np.matmul(BMatrixI.T, self.RElem), BMatrixI))
        self.globalPositionElem = BMatrixI
