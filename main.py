from ReadMatrix import readTransitionMatrix
from nthStepProb import nthStepStates
# from Graph import Graph
from findCB import findCB
from stationaryDist import mergeCB
from ExpectedNumVisits import expectedNumVisits
from CanonicalForm import getCanonical
from HittingProbs import hittingProbs

matrix = readTransitionMatrix()
print(matrix)

nthStepStates(matrix)

cb, residual = findCB(matrix)

mergedMatrix = mergeCB(matrix, cb, residual)
print("Merged Matrix :")
print(mergedMatrix)

standard, Q, R = getCanonical(mergedMatrix)
print("Standard Transition Matrix")
print(standard)
expectedNumVisits(Q)
hittingProbs(Q, R)