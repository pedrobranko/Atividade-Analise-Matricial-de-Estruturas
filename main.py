from src import builder as bd
from src import trussSolve as slv
"""init = inp.InputParametersFromFile("exemplo.txt")
init.openFile()"""

init = bd.InputParametersFromFile('exemplo.txt')
init.readFile()
solve = slv.Solve(init.data)
solve.run()
print("")
