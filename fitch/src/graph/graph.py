
class node:
	
	def __init__(self, data = None):
		
		self.data = data
		
class edge:
	
	def __init__(self, sources, destinations, data = None):
		
		self.sources 	  = sources
		self.destinations = destinations
		self.data = data

class graph:
	
	def __init__(self):
		
		self.root = None
		self.nodes = set()
		self.edges = set()
		
	def add_node(self, data):
		
		nod = node(data)
		self.nodes.add(nod)
		return nod
	
	def add_edge(self, sources, destinations):
		
		'''when adding edges: or you get a nodes from graph, or you are 
		adding new nodes to graph'''
		
		for nod in sources.union(destinations):
			if not nod in self.nodes:
				self.nodes.add(nod)
		
		edg = edge(sources, destinations)
		self.edges.add(edg)

	def get_node(self,  key = None, door = None,):
		
		'''key is the a boolean function'''
								
		for nod in self.nodes:
			if key(nod):
				return nod
				
		return None
		
	def get_edge(self, key):
				
		'''key is the a boolean function'''
								
		for edg in self.edges:
			if key(edg):
				return edg
				
		return None
	
	def by_name(self, name):
		return lambda nod_or_edge: nod_or_edge.name == name
