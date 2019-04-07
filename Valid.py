import numpy as np

def isValidTransitionMatrix(matrix):

	matrix = matrix.values
	matrix = np.round(matrix, decimals = 6)

	if matrix.shape[0] != matrix.shape[1]:
		print("Transition matrix should be a square matrix")
		return False
	
	if not((matrix >= 0).all() and (matrix <= 1).all()):
		print("All elements should be between [0, 1]")
		return False

	rowSum = matrix.sum(axis=1)
	rowSum = np.round(rowSum, decimals = 6)
	
	for idx in range(rowSum.shape[0]):
		if rowSum[idx] != 1:
			print("Sum of row ", idx+1, " is ", rowSum[idx])
			print("Row ", idx+1, " is invalid")
			return 0

	return 1