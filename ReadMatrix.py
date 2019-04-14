from Valid import isValidTransitionMatrix
import pandas as pd

def readTransitionMatrix():
	try:
		matrix = pd.read_csv('matrix.txt', sep=" ", header=None)
		print("Matrix read successfully")
	except:
		print("Matrix Corrupted: Check matrix.txt")
		return -1

	if isValidTransitionMatrix(matrix):
		print("Matrix is a Valid Transition Matrix")
		return matrix.values
	else:
		print("Matrix is not a Valid Transition Matrix")
		return -1
