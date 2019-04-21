import numpy as np

def expectedNumVisits(Q_matrix, states):
	print("*-"*42)
	print("To calculate Expected Number of Visits to transient states before getting absorbed.")
	print("*-"*42)

	I = np.identity(Q_matrix.shape[0], dtype = float)
	N = np.linalg.inv(I-Q_matrix)
	rowSum = N.sum(axis=1)

	# print(N)
	# state = int(input("Enter the starting state (0 indexed): "))
	# if state >= Q_matrix.shape[0] or state < 0:
	# 	print("You should've entered a valid state. Bye!!")
	# 	return -1
	
	for state in range(N.shape[0]):
		print("\nStarting from state", states[state], "expected number of visits in respective states before absorption is :")
		for idx in range(N.shape[0]):
			print("State", states[idx], "expected visits =", N[state][idx])
	
		print("Time till absorption is", rowSum[state], "given we start in state", states[idx])

	return N
