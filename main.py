from ReadMatrix import readTransitionMatrix
from nthStepProb import nthStepStates
from Graph import Graph
from ExpectedNumVisits import expectedNumVisits
from CanonicalForm import getCanonical

matrix = readTransitionMatrix()
print(matrix)

nthStepStates(matrix)

graph = Graph(len(matrix))
graph.adjMatToAdjList(matrix)
cb, cbRev = graph.findSCC()

print("These are the communicating blocks :")
for idx, block in enumerate(cb):
	print("CB", idx+1, ":", end=" ")
	for state in block:
		print(state, end=" ")
	print("")

standard, Q = getCanonical(matrix)
print("Standard Transition Matrix")
print(standard)
expectedNumVisits(Q)
