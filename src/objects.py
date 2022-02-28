import numpy as np


class Material:
    def __init__(self, E=None, S=None, I=None):
        self.id = None
        self.E = E if E is not None else 0
        self.S = S if S is not None else 0
        self.I = I if I is not None else 0

    def setId(self, id):
        self.id = id


class Node:
    def __init__(self, xNode=None, yNode=None, sup=None, fX=None, fY=None, mz=None):
        self.id = None
        self.xNode = xNode if xNode is not None else 0
        self.yNode = yNode if yNode is not None else 0
        self.fX = fX if fX is not None else 0
        self.fY = fY if fY is not None else 0
        self.mz = mz if mz is not None else 0
        self.sup = sup if sup is not None else [0, 0, 0]

    def setId(self, id):
        self.id = id

    def setForces(self, fX, fY):
        self.fX = fX
        self.fY = fY


class Truss:
    def __init__(self, nodes, S=None, E=None):
        self.id = None
        self.nodes = nodes
        self.S = S
        self.E = E
        self.J = [2 * self.nodes[0].id, 2 * self.nodes[0].id + 1]
        self.K = [2 * self.nodes[1].id, 2 * self.nodes[1].id + 1]
        self.L = ((nodes[1].xNode - nodes[0].xNode) ** 2 + ((nodes[1].yNode - nodes[0].yNode) ** 2)) ** .5
        rElem = np.array([[1, 0, -1, 0], [0, 0, 0, 0], [-1, 0, 1, 0], [0, 0, 0, 0]])
        self.rElem = np.multiply(rElem, (self.E * self.S / self.L))
        self.cos = (nodes[1].xNode - nodes[0].xNode) / self.L
        self.sen = (nodes[1].yNode - nodes[0].yNode) / self.L
        self.bElem = np.array([[self.cos, self.sen, 0, 0], [-self.sen, self.cos, 0, 0], [0, 0, self.cos, self.sen],
                               [0, 0, -self.sen, self.cos]])
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


class Bar:
    def __init__(self, nodes, I=None, S=None, E=None, qx=None, qy=None):
        self.id = None
        self.nodes = nodes
        self.I = I if I is not None else 0
        self.S = S if S is not None else 0
        self.E = E if E is not None else 0
        self.qx = qx if qx is not None else 0
        self.qy = qy if qy is not None else 0
        self.J = [3 * self.nodes[0].id, 3 * self.nodes[0].id + 1, 3 * self.nodes[0].id + 2]
        self.K = [3 * self.nodes[1].id, 3 * self.nodes[1].id + 1, 3 * self.nodes[1].id + 2]
        self.L = ((nodes[1].xNode - nodes[0].xNode) ** 2 + ((nodes[1].yNode - nodes[0].yNode) ** 2)) ** .5
        self.rElem = np.array([[self.E * self.S / self.L, 0, 0, self.E * self.S / self.L, 0, 0],
                               [0, 12 * self.E * self.I / self.L ** 3, -6 * self.E * self.I / self.L ** 2, 0,
                                12 * self.E * self.I / self.L ** 3, 6 * self.E * self.I / self.L ** 2],
                               [0, -6 * self.E * self.I / self.L ** 2, 4 * self.E * self.I / self.L, 0,
                                -6 * self.E * self.I / self.L ** 2, -2 * self.E * self.I / self.L],
                               [self.E * self.S / self.L, 0, 0, self.E * self.S / self.L, 0, 0],
                               [0, 12 * self.E * self.I / self.L ** 3, -6 * self.E * self.I / self.L ** 2, 0,
                                12 * self.E * self.I / self.L ** 3, 6 * self.E * self.I / self.L ** 2],
                               [0, 6 * self.E * self.I / self.L ** 2, -2 * self.E * self.I / self.L, 0,
                                6 * self.E * self.I / self.L ** 2, 4 * self.E * self.I / self.L]])
        self.cos = (nodes[1].xNode - nodes[0].xNode) / self.L
        self.sen = (nodes[1].yNode - nodes[0].yNode) / self.L
        self.bElem = np.array([[-self.cos, -self.sen, 0, 0, 0, 0],
                               [-self.sen, self.cos, 0, 0, 0, 0],
                               [0, 0, -1, 0, 0, 0],
                               [0, 0, 0, self.cos, self.sen, 0],
                               [0, 0, 0, self.sen, -self.cos, 0],
                               [0, 0, 0, 0, 0, 1]])
        self.RElem = np.matmul(np.matmul(self.bElem.transpose(), self.rElem), self.bElem)
        self.globalPositionElem = []
        self.RGlobalElem = []

    def setId(self, id):
        self.id = id

    def setElementGlobalParameters(self, nNodes):
        BMatrixI = np.zeros([6, 3 * nNodes])
        BMatrixI[0][self.J[0]] = 1
        BMatrixI[1][self.J[1]] = 1
        BMatrixI[2][self.J[2]] = 1
        BMatrixI[3][self.K[0]] = 1
        BMatrixI[4][self.K[1]] = 1
        BMatrixI[5][self.K[2]] = 1
        self.RGlobalElem = (np.matmul(np.matmul(BMatrixI.T, self.RElem), BMatrixI))
        self.globalPositionElem = BMatrixI
