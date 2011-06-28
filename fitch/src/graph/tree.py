from graph import node, edge, graph
from copy import deepcopy, copy

class tree_node(node):
	
	def __init__(self, name = None):
		
		node.__init__(self) 
		self.sons = set()
		self.father = None
		self.name = name
		
class tree_edge(edge):
	
	def __init__(self, source, destination, data = None):
		
		edge.__init__(self, [source], [destination])
		source.sons.add(destination)
		destination.father = source
		self.source = source
		self.destination = destination

	
class tree(graph):
	
	'''when adding edges: or you get a nodes from graph, or you are 
		adding new nodes to graph'''
	def add_edge(self, source, destination):
	
		for nod in [source] + [destination]:
			if not nod in self.nodes:
				self.nodes.add(nod)
		
		edg = tree_edge(source, destination)
		self.edges.add(edg)
		
	def get_root(self):
		return self.root 

	def copy(self):
		
		t = tree()
		
		for edg in self.edges:
			s = edg.source
			d = edg.destination
			
			s_in_tree = t.get_node(self.by_name(s.name))
			d_in_tree = t.get_node(self.by_name(d.name))
			
			if not s_in_tree: s_in_tree = tree_node(name = s.name)
			if not d_in_tree: d_in_tree = tree_node(name = d.name)
			
			t.add_edge(s_in_tree, d_in_tree)
		
		root = self.get_root()
		new_root = t.get_node(self.by_name(root.name))
		t.root = new_root
		return t


	def get_leaf(self):
		nod = self.get_root()
		while not self.is_leaf(nod):
			for n in nod.sons:
				nod = n
				continue
		return nod
	
	@classmethod
	def is_leaf(self,nod):
		
		if not nod.sons:return True
		return False
	
	@classmethod
	def is_root(self,nod):
	
		if not nod.father:return True
		return False

if __name__ == '__main__':
	

	tr = tree()

	v1 = tree_node(name = 'v1')
	v2 = tree_node(name = 'v2')
	v3 = tree_node(name = 'v3')
	v4 = tree_node(name = 'v4')
	v5 = tree_node(name = 'v5')
	v6 = tree_node(name = 'v6')
	v7 = tree_node(name = 'v7')

	tr.root = v1

	tr.add_edge(v1, v2)
	tr.add_edge(v1, v3)

	tr.add_edge(v2, v4)
	tr.add_edge(v2, v5)

	tr.add_edge(v3, v6)
	tr.add_edge(v3, v7)


	v =  tr.get_leaf()
	
	print v.name






