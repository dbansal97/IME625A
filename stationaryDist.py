import numpy as np

def findStationaryDist(matrix):
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

def extractTransition(matrix, states):
	return matrix[np.ix_(states, states)]

def mergeCB(matrix, cb, residual):
	nMerged = len(cb) + len(residual)
	mergedMatrix = np.zeros((nMerged, nMerged))

	for idx in range(len(cb)):
		mergedMatrix[idx, idx] = 1

	idxRes = list(range(len(cb), nMerged))
	mergedMatrix[np.ix_(idxRes, idxRes)] = matrix[np.ix_(residual, residual)]

	for i, state in enumerate(residual):
		for j, block in enumerate(cb):
			mergedMatrix[i+len(cb), j] = np.sum(matrix[np.ix_([state], block)])

	return mergedMatrix
