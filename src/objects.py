class Node:
    def __init__(self, xNode, yNode, sup=None):
        self.id = None
        self.xNode = xNode
        self.yNode = yNode
        self.sup = sup if sup is not None else [0, 0]

    def setId(self, id):
        self.id = id

class LinStructure:
    def __init__(self, nodes=None, I=None, A=None, E=None):
        self.id = None
        self.nodes = nodes if nodes is not None else []
        self.I = I
        self.A = A
        self.E = E

    def setId(self, id):
        self.id = id