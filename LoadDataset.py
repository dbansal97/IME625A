import numpy as np

def loadPageRankData():

	filename = "hollins.dat"
	with open(filename) as fn:
	    content = fn.readlines()

	states = {}

	for idx in range(1, 6013):
		stateNum, stateName = content[idx].split()
		states[int(stateNum)-1] = stateName

	matrix = np.zeros((6012, 6012))

	for idx in range(6013, 29888):
		u, v = content[idx].split()
		u = int(u) - 1
		v = int(v) - 1
		matrix[u][v] = 1

	rowSum = matrix.sum(axis=1)
	for idx in range(rowSum.shape[0]):
		if rowSum[idx] != 0:
			matrix[idx] = matrix[idx]/rowSum[idx]
		else:
			matrix[idx][idx] = 1

	return states, matrix
