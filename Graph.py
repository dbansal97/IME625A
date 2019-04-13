from collections import defaultdict

class Graph:
	def __init__(self, nVert):
		self.V = nVert
		self.graph = defaultdict(list)

	def connect(self, u, v):
		self.graph[u].append(v)

	def DFS(self, v, visited, startOrd, finOrd):
		visited[v] = True
		startOrd.append(v)
		for u in self.graph[v]:
			if not visited[u]:
				self.DFS(u, visited)
		finOrd.append(v)

	def getTranspose(self):
		newGraph = Graph(self.V)
		for u in self.graph:
			for v in self.graph[u]:
				newGraph.connect(v, u)
		return newGraph

	def findSCC(self):
		scc = []
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
				gr.DFS(v, visited, startOrd, [])
				scc.append(startOrd)

		return scc
