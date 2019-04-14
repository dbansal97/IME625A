from ReadMatrix import readTransitionMatrix
from nthStepProb import nthStepStates
# from Graph import Graph
from findCB import findCB
from ExpectedNumVisits import expectedNumVisits
from CanonicalForm import getCanonical
from HittingProbs import hittingProbs

matrix = readTransitionMatrix()
print(matrix)

nthStepStates(matrix)

findCB(matrix)

standard, Q, R = getCanonical(matrix)
print("Standard Transition Matrix")
print(standard)
expectedNumVisits(Q)
hittingProbs(Q, R)