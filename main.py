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
print(matrix, "\n")
print("Input Starting Distribution :")
print(startDist, "\n")

# nthStepStates(matrix)

cb, residual = findCB(matrix)

mergedMatrix = mergeCB(matrix, cb, residual)
print("Merged Matrix :")
print(mergedMatrix, "\n")

standard, Q, R, states = getCanonical(mergedMatrix, cb, residual)
print("Standard Transition Matrix :")
print(standard, "\n")
print("States :")
print(states, "\n")

expNumVisits = expectedNumVisits(Q, states)
hitProb = hittingProbs(Q, R, states)

stationaryDist = findStationaryDistOverAll(matrix, startDist, states, hitProb)
print("\nStationary Distribution :")
print(stationaryDist, "\n")
