import copy
class Graph:

	def __init__(self, graph):
		self.graph = graph # residual graph
		self.ROW = len(graph)

	def BFS(self, s, t, parent):

		visited = [False]*(self.ROW)

		# Create a queue for BFS
		queue = []
		queue.append(s)
		visited[s] = True
		while queue:
			u = queue.pop(0)
			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0:
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u
					if ind == t:
						return True
		return False # No augmenting path is found
			
	def FordFulkerson(self, source, sink):
		parent = [-1]*(self.ROW)
		max_flow = 0
		while self.BFS(source, sink, parent):
			path_flow = float("Inf") # Set this to either 0 or inf
			s = sink
			while(s != source):
				path_flow = min (path_flow, self.graph[parent[s]][s])
				s = parent[s]
			max_flow += path_flow
			v = sink
			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]
		return max_flow

def add_dummy_node(entrances, exits, path):
    # Initialise dummy entrance node
    path.insert(0, [0] * len(path)) 
    for ls in path:
        ls.insert(0, 0)
    entrances = [i + 1 for i in entrances]
    d = {k:sum(v) for k,v in list(enumerate(path)) if k in entrances}
    path[0] = [d[x] if x in d.keys() else 0 for x in range(len(path[0]))] 

    # Initialise dummy exit node
    path.append([0] * len(path)) #
    for ls in path:
        ls.append(0)
    exits = [i + 1 for i in exits]
    for ex in exits:
        path[ex][-1] = float('inf')
    return path

def solution(entrances, exits, path):
	entrances = copy.deepcopy(entrances)
	exits = copy.deepcopy(exits)
	path = copy.deepcopy(path)
	
	# Check if single-source single-sink
	if len(entrances) != 1 or len(exits) != 1: 
		path = add_dummy_node(entrances, exits, path)
		source = 0
		sink = (len(path)-1)
	# If yes, continue as usual
	else:
		source = entrances[0]
		sink = exits[0]
	g = Graph(path)
	
	return int(g.FordFulkerson(source, sink))
