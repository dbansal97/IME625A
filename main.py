from ReadMatrix import readTransitionMatrix
from nth_stepProbabilities import nth_step_states

matrix = readTransitionMatrix()
print(matrix)

nth_step_states(matrix)
