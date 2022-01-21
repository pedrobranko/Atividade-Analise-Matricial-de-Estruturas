class Data:
    def __init__(self):
        self.materialList = []
        self.nodeList = []
        self.linStructureList = []
        self.globalForces = []
        self.prescribedNodes = []

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

    def addTruss(self, linSructure):
        linSructure = linSructure
        idLin = len(self.linStructureList) if len(self.linStructureList) != 0 else 0
        linSructure.setId(idLin)
        self.linStructureList.append(linSructure)

    def getGlobalForces(self):
        for i in range(len(self.nodeList)):
            self.globalForces.append(self.nodeList[i].fX)
            self.globalForces.append(self.nodeList[i].fY)

    def getPrescribedNodes(self):
        for i in range(len(self.nodeList)):
            if self.nodeList[i].sup[0] == 1:
                self.prescribedNodes.append(2 * i)
            if self.nodeList[i].sup[1] == 1:
                self.prescribedNodes.append(2 * i + 1)
