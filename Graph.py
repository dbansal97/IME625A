from collections import defaultdict
import numpy as np

class Graph:
	def __init__(self, nVert):
		self.V = nVert
		self.adjList = defaultdict(list)

	def connect(self, u, v):
		self.adjList[u].append(v)

	def adjMatToAdjList(self, mat):
		self.V = len(mat)
		for i in range(self.V):
			for j in range(self.V):
				if mat[i][j]:
					self.connect(i, j)

	def DFS(self, v, visited, startOrd, finOrd):
		visited[v] = True
		startOrd.append(v)
		for u in self.adjList[v]:
			if not visited[u]:
				self.DFS(u, visited, startOrd, finOrd)
		finOrd.append(v)

	def getTranspose(self):
		newGraph = Graph(self.V)
		for u in self.adjList:
			for v in self.adjList[u]:
				newGraph.connect(v, u)
		return newGraph

	def findSCC(self):
		scc = []
		sccRevMap = np.zeros(self.V, np.int)
		finOrd = []
		visited = [False] * (self.V)
		for v in range(self.V):
			if not visited[v]:
				self.DFS(v, visited, [], finOrd)

		graphT = self.getTranspose()

		visited = [False] * (self.V)

		while finOrd:
			v = finOrd.pop()
			if not visited[v]:
				startOrd = []
				graphT.DFS(v, visited, startOrd, [])
				sccRevMap[startOrd] = len(scc)
				scc.append(startOrd)

		scc = np.sort(np.asarray(scc))
		
		return scc, sccRevMap

	def printSCC(self):
		cb, _ = self.findSCC()
		print("These are the communicating blocks :")
		for idx, block in enumerate(cb):
			print("CB", idx+1, ":", end=" ")
			for state in block:
				print(state, end=" ")
			print("")
