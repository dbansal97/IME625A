from Graph import Graph
import numpy as np

def findCB(matrix):
	graph = Graph(len(matrix))
	graph.adjMatToAdjList(matrix)

	scc, _ = graph.findSCC()

	residual = []
	cb = []

	for block in scc:
		isCB = True
		for state in block:
			for neighbour in graph.adjList[state]:
				if neighbour not in block:
					residual.extend(block)
					isCB = False
					break

			if not isCB:
				break

		if isCB:
			cb.append(block)

	cbRev = np.zeros(graph.V, np.int)

	for idx, block in enumerate(cb):
		cbRev[block] = idx

	cbRev[residual] = len(cb)

	print("These are the communicating blocks :")
	for idx, block in enumerate(cb):
		print("CB", idx+1, ":", end=" ")
		for state in block:
			print(state, end=" ")
		print("")

	print("These are the residual states :")
	for state in residual:
		print(state, end=" ")
	print("")

	return cb, residual
