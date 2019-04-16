from ReadMatrix import readSpecs
from nthStepProb import nthStepStates
from findCB import findCB
from mergeCB import mergeCB
from stationaryDist import findStationaryDistOverAll
from ExpectedNumVisits import expectedNumVisits
from CanonicalForm import getCanonical
from HittingProbs import hittingProbs
from LoadDataset import loadPageRankData
import numpy as np
from decimal import Decimal

def printPages(stationaryDist, stateNames, numPages = 10):
	stationaryDist = stationaryDist.reshape(stationaryDist.shape[0])
	indicies = stationaryDist.argsort()[-numPages:][::-1]

	for idx in range(indicies.shape[0]):
		print("Page at Rank ", idx+1, " is ", stateNames[indicies[idx]],\
		 " with probability ", round(Decimal(stationaryDist[indicies[idx]]), 7))

def pagerankWiki(M, startDist, eps=1.0e-4, d=0.85):
    N = M.shape[1]
    v = np.random.rand(N, 1)
    # v = startDist
    v = v / np.linalg.norm(v, 1)
    last_v = np.ones((N, 1), dtype=np.float32) * 100

def pagerankWiki(M, eps=1.0e-8, d=0.85):
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    last_v = np.ones((N, 1), dtype=np.float32) * 100
    
    while np.linalg.norm(v - last_v, 2) > eps:
        last_v = v
        v = d * np.matmul(M, v) + (1 - d) / N
    return v

def ourPageRank(stateNames, matrix, startDist):
	cb, residual = findCB(matrix)

	mergedMatrix = mergeCB(matrix, cb, residual)
	
	np.save("cb", cb)
	np.save("residual", residual)
	np.save("mergedMatrix", mergedMatrix)

	print("Merged Matrix :")
	print(mergedMatrix)

	standard, Q, R, states = getCanonical(mergedMatrix, cb, residual)
	print("Standard Transition Matrix :")
	print(standard)
	print("States :")
	print(states)

	np.save("standard", standard)
	np.save("Q", Q)
	np.save("R", R)
	np.save("states", states)

	expectedNumVisits(Q, states)
	hitProb = hittingProbs(Q, R, states)

	np.save("hitProb", hitProb)

	expectedNumVisits(Q, states)
	hitProb = hittingProbs(Q, R, states)

	stationaryDist = findStationaryDistOverAll(matrix, startDist, states, hitProb)
	print("Stationary Distribution :")
	print(stationaryDist)

def Loaded(matrix, startDist):
	cb = np.load("cb.npy")
	residual = np.load("residual.npy")
	mergedMatrix = np.load("mergedMatrix.npy")
	
	# print("Merged Matrix :")
	# print(mergedMatrix)

	standard = np.load("standard.npy")
	Q = np.load("Q.npy")
	R = np.load("R.npy")
	states = np.load("states.npy")
	
	# print("Standard Transition Matrix :")
	# print(standard)
	# print("States :")
	# print(states)

	# expectedNumVisits(Q, states)
	hitProb = hittingProbs(Q, R, states)

	np.save("hitProb", hitProb)
	
	stationaryDist = findStationaryDistOverAll(matrix, startDist, states, hitProb)
	# print("Stationary Distribution :")
	# print(stationaryDist)
	return stationaryDist

def main():
	stateNames, matrix = loadPageRankData()
	startDist = np.zeros(matrix.shape[0])
	startDist.fill(1/matrix.shape[0])

	print("Going for Loaded")
	ourStationary = Loaded(matrix, startDist)
	print("Going for Wiki")
	wikiStationary = pagerankWiki(matrix.T, startDist)
	
	print("For Wiki")
	printPages(wikiStationary, stateNames)
	print(wikiStationary)


	print("For Us")
	printPages(ourStationary, stateNames)
	print(ourStationary)

def printPages(stationaryDist, stateNames, numPages = 10):
	stationaryDist = stationaryDist.reshape(stationaryDist.shape[0])
	indicies = stationaryDist.argsort()[-numPages:][::-1]

	for idx in range(indicies.shape[0]):
		print("Page at Rank ", idx+1, " is ", stateNames[indicies[idx]],\
		 " with probability ", round(Decimal(stationaryDist[indicies[idx]]), 7))


def main():
	stateNames, matrix = loadPageRankData()

	v = pagerankWiki(matrix.T)
	print(v)
	
	printPages(v, stateNames)
	# startDist = np.zeros(matrix.shape[0])
	# startDist.fill(1/matrix.shape[0])
	# print(startDist)
	# ourPageRank(stateNames, matrix, startDist)

if __name__ == "__main__":
	main()