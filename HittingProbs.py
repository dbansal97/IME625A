import numpy as np

def hittingProbs(Q_matrix, R_matrix, states):
	print("*-"*55)
	print("To calculate starting from certain transient state what is probability of gettin absorbed in absorbing states.")
	print("*-"*55)

	I = np.identity(Q_matrix.shape[0], dtype=float)
	N = np.linalg.inv(I-Q_matrix)

	B = np.matmul(N, R_matrix)

	state = int(input("Enter the starting state (0 indexed): "))
	if state >= Q_matrix.shape[0] or state < 0:
		print("You should've entered a valid state. Bye!!")
		return -1

	print("Starting from state", state, "prob. of absorption in different absorbing states is :")
	for idx in range(B.shape[1]):
		print("State", states[idx+B.shape[1]], "absorption prob. =", B[state][idx])
	
	idxTrans = list(range(0, Q_matrix.shape[0]))
	idxAbs = list(range(Q_matrix.shape[0], len(states)))
	hitProb = np.zeros((len(states), len(states)))
	hitProb[np.ix_(idxAbs, idxAbs)] = np.eye(R_matrix.shape[1])
	hitProb[np.ix_(idxTrans, idxAbs)] = B

	return hitProb