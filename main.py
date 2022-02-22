from src import builder as bd
from src import trussSolve as slv
from src import output as out

inputName = input("Insira o nome do arquivo: ")
init = bd.InputParametersFromFile(inputName)
init.readFile()
solve = slv.Solve(init.data)
solve.solveTruss()
out = out.Output(init.data, solve)
out.outputFile(inputName)

