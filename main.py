from ReadMatrix import readTransitionMatrix
from nthStepProb import nthStepStates
from Graph import Graph
from ExpectedNumVisits import expectedNumVisits

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

expectedNumVisits(matrix)
