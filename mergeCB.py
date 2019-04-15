import numpy as np

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
