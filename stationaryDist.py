import numpy as np

def findStationaryDistCB(matrix):
	# Solve (A^T - I) X  = 0 where X is the stationary distribution
	# along with the equation x + y = 1
	# A is the transition matrix of finite irreducible Markov Chain
	n = len(matrix)
	B = matrix.T-np.eye(n)
	B[-1] = np.ones(n)
	C = np.zeros(n)
	C[-1] = 1
	X = np.linalg.solve(B, C)

	return X

def findStationaryDistOverAll(matrix, startDist, states, hitProb):
	mergedStartDist = np.zeros(len(states))
	for idx, state in enumerate(states):
		mergedStartDist[idx] = startDist[state].sum()

	mergedStationary = np.matmul(mergedStartDist, hitProb)

	stationaryDist = np.zeros(len(startDist))
	for idx, state in enumerate(states):
		if mergedStationary[idx] == 0:
			continue

		stDist = findStationaryDistCB(matrix[np.ix_(state, state)])
		stationaryDist[state] = mergedStationary[idx] * stDist

	return stationaryDist
