class Builder:
    def __init__(self):
        self.nodeList = []
        self.nodeIdList = []
        self.linStructureList = []
        self.linStructureIdList = []

    def addNode(self, node):
        node = node
        idNode = len(self.nodeIdList) if len(self.nodeIdList) != 0 else 0
        node.setId(idNode)
        self.nodeList.append(node)
        self.nodeIdList.append(idNode)

    def addTruss(self, linSructure):
        linSructure = linSructure
        idLin = len(self.linStructureIdList) if len(self.linStructureIdList) != 0 else 0
        linSructure.setId(idLin)
        self.linStructureList.append(linSructure)
        self.linStructureIdList.append(idLin)
