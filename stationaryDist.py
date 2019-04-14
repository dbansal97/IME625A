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