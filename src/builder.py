from src import objects as obj
from src import data as dt
import matplotlib.pyplot as plt


class InputParametersFromFile:
    def __init__(self, filename):
        self.filename = filename
        self.data = dt.Data()

    def readFile(self):
        file = open(self.filename, "r")
        aux = ''

        while True:
            aux = file.readline()

            if aux == "#MATERIAL\n":
                aux = file.readline()
                aux = file.readline()
                nMaterials = int(aux.split("\n")[0])
                aux = file.readline()
                for i in range(nMaterials):
                    aux = file.readline()
                    aux = aux.split("\t")
                    idMaterial = int(aux[0])
                    E = float(aux[1])
                    S = float(aux[2])
                    material = obj.Material(E=E, S=S)
                    material.setId(idMaterial)
                    self.data.addMaterial(material)

            if aux == "#NODE\n":
                aux = file.readline()
                aux = file.readline()
                nNodes = int(aux.split("\n")[0])
                aux = file.readline()
                for i in range(nNodes):
                    aux = file.readline()
                    aux = aux.split("\t")
                    idNode = int(aux[0])
                    xNode = float(aux[1])
                    yNode = float(aux[2])
                    xSuport = float(aux[3])
                    ySuport = float(aux[4])
                    fX = float(aux[5])
                    fY = float(aux[6])
                    node = obj.Node(xNode=xNode, yNode=yNode, sup=[xSuport, ySuport], fX=fX, fY=fY)
                    node.setId(idNode)
                    self.data.addNode(node)

            if aux == "#TRUSS\n":
                aux = file.readline()
                aux = file.readline()
                nTruss = int(aux.split("\n")[0])
                aux = file.readline()
                for i in range(nTruss):
                    aux = file.readline()
                    aux = aux.split("\t")
                    id = aux[0]
                    material = self.data.materialList[int(aux[1])]
                    n1 = self.data.nodeList[int(aux[2])]
                    n2 = self.data.nodeList[int(aux[3])]
                    truss = obj.Truss(nodes=[n1, n2], E=material.E, S=material.S)
                    truss.setId(id)
                    self.data.addTruss(truss)

            if aux == "#END":
                file.close()
                self.data.setGlobalForces()
                self.data.setPrescribedNodes()
                self.data.setGlobalKMatrix()
                break


class InputParameters:
    def __init__(self):
        self.build = dt.Data()

    def inputParameters(self):
        count = 0
        while (True):
            inputVariable = input(
                "Escolha uma opção: \n\t[1] Adicionar ponto \n\t[2] Adicionar seguimento \n\t[3] Visualizar"
                " \n\t[4] Salvar e Finalizar \n\t[5] Finalizar\n")

            if int(inputVariable) == 1:
                xnode = input("Entre com o Valor de X: ")
                ynode = input("Entre com o Valor de Y: ")
                node = obj.Node(xNode=float(xnode), yNode=float(ynode))
                self.build.addNode(node)
                count += 1

            if int(inputVariable) == 2 and count > 1:
                node1Id = int(input("Entre com o id do Primeiro Ponto: "))
                node2Id = int(input("Entre com o id do Segundo Ponto: "))
                if int(node1Id) == int(node2Id):
                    print("\nParâmetro Inválido: Insira ID's diferentes")

                else:
                    linStr = obj.Truss(nodes=[self.build.nodeList[node1Id], self.build.nodeList[node2Id]])
                    self.build.addTruss(linStr)
            '''else:
                print("\nParâmetro Inválido: Defina dois pontos ou mais\n")'''

            if int(inputVariable) == 3 and count >= 1:
                xNodes = []
                yNodes = []
                nodeIdList = []

                for i in range(0, len(self.build.nodeList)):
                    xNodes.append(self.build.nodeList[i].xNode)
                    yNodes.append(self.build.nodeList[i].yNode)
                    nodeIdList.append(self.build.nodeList[i])
                fig, ax = plt.subplots()
                ax.scatter(xNodes, yNodes)
                for i, txt in enumerate(nodeIdList):
                    ax.annotate(txt, (xNodes[i] + .03, yNodes[i] + .03))
                plt.show()

            if int(inputVariable) == 5:
                return
