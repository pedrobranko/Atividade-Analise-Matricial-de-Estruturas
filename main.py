import matplotlib.pyplot as plt


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

    def addLinStructure(self, linSructure):
        linSructure = linSructure
        idLin = len(self.linStructureIdList) if len(self.linStructureIdList) != 0 else 0
        linSructure.setId(idLin)
        self.linStructureList.append(linSructure)
        self.linStructureIdList.append(idLin)


class InputParameters:
    def __init__(self):
        self.build = Builder()

    def inputParameters(self):
        count = 0
        while (True):
            inputVariable = input(
                "Escolha uma opção: \n\t[1] Adicionar ponto \n\t[2] Adicionar seguimento \n\t[3] Visualizar"
                " \n\t[4] Salvar e Finalizar \n\t[5] Finalizar\n")

            if int(inputVariable) == 1:
                xnode = input("Entre com o Valor de X: ")
                ynode = input("Entre com o Valor de Y: ")
                node = Node(xNode=float(xnode), yNode=float(ynode))
                self.build.addNode(node)
                count += 1

            if int(inputVariable) == 2 and count > 1:
                node1Id = int(input("Entre com o id do Primeiro Ponto: "))
                node2Id = int(input("Entre com o id do Segundo Ponto: "))
                if int(node1Id) == int(node2Id):
                    print("\nParâmetro Inválido: Insira ID's diferentes")

                else:
                    linStr = LinStructure(nodes=[self.build.nodeList[node1Id], self.build.nodeList[node2Id]])
                    self.build.addLinStructure(linStr)
            '''else:
                print("\nParâmetro Inválido: Defina dois pontos ou mais\n")'''

            if int(inputVariable) == 3 and count >= 1:
                xNodes = []
                yNodes = []
                nodeIdList = []

                for i in range(0, len(self.build.nodeIdList)):
                    xNodes.append(self.build.nodeList[i].xNode)
                    yNodes.append(self.build.nodeList[i].yNode)
                    nodeIdList.append(self.build.nodeIdList[i])
                fig, ax = plt.subplots()
                ax.scatter(xNodes, yNodes)
                for i, txt in enumerate(nodeIdList):
                    ax.annotate(txt, (xNodes[i]+ .03, yNodes[i] + .03))
                plt.show()

            if int(inputVariable) == 5: return

class inputParametersFromFile:
    def __init__(self, filename):
        self.filename = filename
        self.build = Builder()

    def openFile(self):
        file = open(self.filename, "r")
        aux = ''

        while True:
            aux = file.readline()
            if aux == "#NODE\n":
                nNodes = int(file.readline())
                for i in range(0, nNodes):
                    aux = file.readline()
                    idNode = int(aux[0])
                    xNode = float(aux[2])
                    yNode = float(aux[4])
                    xSuport = float(aux[6])
                    ySuport = float(aux[8])
                    node = Node(xNode, yNode, [xSuport, ySuport])
                    node.setId(idNode)
                    self.build.addNode(node)

            break

        print('')





init = inputParametersFromFile("exemplo.txt")
init.openFile()
