from ReadMatrix import readSpecs
from nthStepProb import nthStepStates
from findCB import findCB
from mergeCB import mergeCB
from stationaryDist import findStationaryDistOverAll
from ExpectedNumVisits import expectedNumVisits
from CanonicalForm import getCanonical
from HittingProbs import hittingProbs

matrix, startDist = readSpecs()
print("Input Transition Matrix :")
print(matrix)
print("Input Starting Distribution :")
print(startDist)

# nthStepStates(matrix)

cb, residual = findCB(matrix)

mergedMatrix = mergeCB(matrix, cb, residual)
print("Merged Matrix :")
print(mergedMatrix)

standard, Q, R, states = getCanonical(mergedMatrix, cb, residual)
print("Standard Transition Matrix :")
print(standard)
print("States :")
print(states)

expectedNumVisits(Q, states)
hitProb = hittingProbs(Q, R, states)

stationaryDist = findStationaryDistOverAll(matrix, startDist, states, hitProb)
print("Stationary Distribution :")
print(stationaryDist)