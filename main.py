from ReadMatrix import readTransitionMatrix
from nthStepProb import nthStepStates

matrix = readTransitionMatrix()
print(matrix)

nthStepStates(matrix)
