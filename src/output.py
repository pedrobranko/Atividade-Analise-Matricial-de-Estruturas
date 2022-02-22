class Output():
    def __init__(self, data, solve):
        self.data = data
        self.solve = solve

    def outputFile(self, filename):
        filename = filename[:-4] + "_results.txt"
        file = open(filename, "w")

        file.write("Dados Nodais:\n")
        for i in range(len(self.data.nodeList)):
            id = self.data.nodeList[i].id
            file.write("#id: " + str(id) + "\t")
            aux = "#des.X: {:.4e}\t"
            file.write(aux.format(self.solve.globalDisplacement[2 * id]))
            aux = "#des.Y: {:.4e}\t"
            file.write(aux.format(self.solve.globalDisplacement[2 * id + 1]))
            file.write("\n")

        file.write("\n")

        file.write("Dados das Barras:\n")
        for i in range(len(self.data.linStructureList)):
            id = self.data.linStructureList[i].id
            file.write("#id: " + str(id) + "\t")
            aux = "#Normal: {:.4e}\t"
            file.write(aux.format(self.solve.internalForces[id][2]))
            file.write("\n")

        file.write("\n")

        file.write("Reacoes de Apoio:\n")
        for i in range(len(self.solve.supportForces)):
            aux = "#No: {}\t"
            file.write(aux.format(int((self.solve.supportForces[i][0] / 2))))
            aux = "RX: {:.4e}\t" + "RY: {:.4e}\n"
            file.write(aux.format(self.solve.supportForces[i][1][0], self.solve.supportForces[i][1][1]))
            file.write("\n")

        file.write("\n")

        file.close()
