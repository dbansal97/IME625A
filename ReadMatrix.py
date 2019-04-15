import numpy as np

def isValidTransitionMatrix(matrix):
	matrix = np.round(matrix, decimals=6)

	if matrix.shape[0] != matrix.shape[1]:
		print("Transition matrix should be a square matrix")
		return False
	
	if not((matrix >= 0).all() and (matrix <= 1).all()):
		print("Transition Matrix : All elements should be between [0, 1]")
		return False

	rowSum = matrix.sum(axis=1)
	rowSum = np.round(rowSum, decimals = 6)
	
	for idx in range(rowSum.shape[0]):
		if rowSum[idx] != 1:
			print("Sum of row ", idx+1, " is ", rowSum[idx])
			print("Row ", idx+1, " is invalid")
			return False

	return True

def isValidStartingDist(startDist):
	startDist = np.round(startDist, decimals=6)

	if startDist.shape != (len(startDist), ):
		print("Improper Starting Distribution (Dimension error : Not (n, ))")
		return False

	if not ((startDist >= 0).all() and (startDist <= 1).all()):
		print("Starting Distribution : All elements should be in between [0, 1]")
		return False

	if startDist.sum() != 1:
		print("Sum of starting distribution should be 1")
		return False

	return True

def readTransitionMatrix():
	try:
		matrix = np.genfromtxt('matrix.txt')
		print("Matrix read successfully")
	except:
		print("Matrix Corrupted: Check matrix.txt")
		return -1

	if isValidTransitionMatrix(matrix):
		print("Matrix is a Valid Transition Matrix")
		return matrix

	print("Matrix is not a Valid Transition Matrix")
	return -1

def readStartingDist():
	try:
		startDist = np.genfromtxt('start.txt')
		print("Start Distribution read successfully")
	except:
		print("File Corrupted: Check start.txt")
		return -1

	if isValidStartingDist(startDist):
		print("Valid Starting Distribution")
		return startDist

	print("Invalid Starting Distribution")
	return -1


def readSpecs():
	matrix = readTransitionMatrix()
	startDist = readStartingDist()

	if matrix.shape[0] != startDist.shape[0]:
		print("Dimensions of starting distribution and transition matrix don't match.")
		return -1, -1

	return matrix, startDist
