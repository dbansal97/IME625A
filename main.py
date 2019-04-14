from ReadMatrix import readTransitionMatrix
from nthStepProb import nthStepStates
# from Graph import Graph
from findCB import findCB
from ExpectedNumVisits import expectedNumVisits

matrix = readTransitionMatrix()
print(matrix)

nthStepStates(matrix)

findCB(matrix)

expectedNumVisits(matrix)
