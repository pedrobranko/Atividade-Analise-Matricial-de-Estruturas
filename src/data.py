class Data:
    def __init__(self):
        self.materialList = []
        self.nodeList = []
        self.linStructureList = []
        self.globalForces = []
        self.prescribedNodes = []
        self.RGlobal = []

    def addMaterial(self, material):
        material = material
        idMaterial = len(self.materialList) if len(self.materialList) != 0 else 0
        material.setId(idMaterial)
        self.materialList.append(material)

    def addNode(self, node):
        node = node
        idNode = len(self.nodeList) if len(self.nodeList) != 0 else 0
        node.setId(idNode)
        self.nodeList.append(node)

    def addLinStructure(self, linSructure):
        linSructure = linSructure
        idLin = len(self.linStructureList) if len(self.linStructureList) != 0 else 0
        linSructure.setId(idLin)
        self.linStructureList.append(linSructure)

    def setTrussGlobalForces(self):
        for i in range(len(self.nodeList)):
            self.globalForces.append(self.nodeList[i].fX)
            self.globalForces.append(self.nodeList[i].fY)

    def setFrameGlobalForces(self):
        for i in range(len(self.nodeList)):
            self.globalForces.append(self.nodeList[i].fX)
            self.globalForces.append(self.nodeList[i].fY)
            self.globalForces.append(self.nodeList[i].mz)


    def setPrescribedNodes(self):
        for i in range(len(self.nodeList)):
            if self.nodeList[i].sup[0] == 1:
                self.prescribedNodes.append(2 * i)
            if self.nodeList[i].sup[1] == 1:
                self.prescribedNodes.append(2 * i + 1)

    def setGlobalKMatrix(self):
        self.linStructureList[0].setElementGlobalParameters(len(self.nodeList))
        self.RGlobal = self.linStructureList[0].RGlobalElem.copy()

        for i in range(1, len(self.linStructureList)):
            self.linStructureList[i].setElementGlobalParameters(len(self.nodeList))
            self.RGlobal += self.linStructureList[i].RGlobalElem.copy()

    @property
    def getGlobalForces(self):
        globalForces = self.globalForces.copy()
        return globalForces

    @property
    def getPrescribedNodes(self):
        prescribedNodes = self.prescribedNodes.copy()
        return prescribedNodes

    @property
    def getRGlobal(self):
        RGlobal = self.RGlobal.copy()
        return RGlobal
