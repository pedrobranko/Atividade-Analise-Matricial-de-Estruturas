import numpy as np


class Solve:
    def __init__(self, data):
        self.data = data
        self.RGlobalPenalty = []
        self.globalForcesPenalty = []
        self.prescribedNodes = self.data.getPrescribedNodes
        self.globalDisplacement = []
        self.internalForces = []
        self.supportForces = []

    def setPenalty(self):
        count = 0
        RGlobalPenalty = self.data.getRGlobal
        globalForcesPenalty = self.data.getGlobalForces
        for i in range(len(globalForcesPenalty)):
            if count < len(self.prescribedNodes) and i == self.prescribedNodes[count]:
                RGlobalPenalty[i][i] *= 1e6
                globalForcesPenalty[i] *= 1e6
                count += 1
        self.RGlobalPenalty = RGlobalPenalty
        self.globalForcesPenalty = globalForcesPenalty

    def setGlobalDisplacemente(self):
        RGlobalpenalty = self.RGlobalPenalty.copy()
        globalForcesPenalty = self.globalForcesPenalty.copy()
        globalDisplacement = np.matmul(np.linalg.inv(RGlobalpenalty), np.transpose(globalForcesPenalty))
        self.globalDisplacement = globalDisplacement

    def setInternalForces(self):
        internalForces = []
        for elem in self.data.linStructureList:
            DJ1 = self.globalDisplacement[elem.J[0]].copy()
            DJ2 = self.globalDisplacement[elem.J[1]].copy()
            DK1 = self.globalDisplacement[elem.K[0]].copy()
            DK2 = self.globalDisplacement[elem.K[1]].copy()
            DGlobalElem = np.array([DJ1, DJ2, DK1, DK2])
            DLocalElem = np.matmul(elem.bElem.copy(), DGlobalElem)
            NElem = np.matmul(elem.rElem.copy(), DLocalElem)
            internalForces.append(NElem)
        self.internalForces = np.array(internalForces)

    def setSupportForces(self):
        for sup in self.data.prescribedNodes:
            supFor = [0, 0]
            for elem in self.data.linStructureList:
                for i in [0, 1]:
                    if elem.J[i] == sup:
                        if i == 0:
                            supFor[i] -= self.internalForces[elem.id][2] * abs(elem.cos)
                        else:
                            supFor[i] -= self.internalForces[elem.id][2] * abs(elem.sen)
                    if elem.K[i] == sup:
                        if i == 0:
                            supFor[i] -= self.internalForces[elem.id][2] * abs(elem.cos)
                        else:
                            supFor[i] -= self.internalForces[elem.id][2] * abs(elem.sen)
            self.supportForces.append([sup, supFor])

    def run(self):
        self.setPenalty()
        self.setGlobalDisplacemente()
        self.setInternalForces()
        self.setSupportForces()
