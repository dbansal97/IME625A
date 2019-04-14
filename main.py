from ReadMatrix import readTransitionMatrix
from nthStepProb import nthStepStates
from ExpectedNumVisits import expectedNumVisits

matrix = readTransitionMatrix()
print(matrix)

nthStepStates(matrix)
expectedNumVisits(matrix)