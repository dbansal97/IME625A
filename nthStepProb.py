from numpy.linalg import matrix_power
import numpy as np

def nthStepStates(matrix):
	
	state = int(input("Enter the starting state (0 indexed): "))
	if state >= matrix.shape[0] or state < 0:
		print("You should've entered a valid state. Bye!!")
		return -1
	
	steps = int(input("Enter the number of steps: "))
	if steps <= 0:
		print("You should've entered valid number of steps. Bye!!")
		return -1

	newMatrix = matrix_power(matrix, steps)

	print("Starting from state ", state, " we have following probs after ", steps, " steps")
	for idx in range(newMatrix.shape[0]):
		print("State ", idx, " with prob. = ", newMatrix[state][idx])
	
	return 1
