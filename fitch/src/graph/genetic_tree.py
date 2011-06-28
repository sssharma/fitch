from tree import tree_node as node
from tree import tree_node
from tree import tree_edge as egde
from tree import tree
from copy import deepcopy

class specie(tree_node):
	
	def __init__(self, r = None, name = None, theta = None):
		
		node.__init__(self)
		self.R = set()
		self.name = name
		self.theta = theta
		
		if r: 
			self.r =  r
			self.R.add(r)
		else:
			self.r = None

	def copy(self):
		s = specie(self.r, self.name)
		s.R = self.R
		return s

class genetic_tree(tree):
	
	def copy(self):
		
		t = genetic_tree()
		
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
		
		for specie in self.nodes:
			new_tree_specie = t.get_node(self.by_name(specie.name))
			new_tree_specie.r = specie.r
			new_tree_specie.R = set(specie.R)
		
		return t
	
	def __cmp__(self, other):
		return cmp(self.__str__(), other.__str__())
		
	def __hash__(self):
		return id(self)
	
	def __repr__(self):
		return str(dict((node.name, node.r ) for node in self.nodes))
		
	def __str__(self):
		return str(self.__repr__())

