from genetic_tree import genetic_tree 
from genetic_tree import specie
from tree import tree


class fitch_tree(tree):
	
	def __init__(self, tr):
		
		self.gtr = tr
		self.possible_r_trees = []
		self.possible_trees = set()
		self.len = len(self.gtr.get_leaf().r)
		
		for i in range(self.len):

			index_tree = self.gtr.copy()
			for node in index_tree.nodes:

				if node.r: 

					node.r = node.r[i]
					node.R = set([node.r])

			self.R(index_tree)
			self.possible_r_trees.append(set([index_tree]))
			self.r(index_tree.get_root(),index_tree, self.possible_r_trees[i])
		
	def get_possible_trees(self, list_of_sets_of_trees):
		
		if not list_of_sets_of_trees: return 
		
		for tree in list_of_sets_of_trees[0]:
			
			self.possible_trees = self.possible_trees.union( self.get_possible_trees(list_of_sets_of_trees[1:]))
	
	def R(self, tr):
		
		def helper(node):
			
			if node.r: 
				return node.R
			else: 
				inter = set()
				union = set()
				for son in node.sons:
					if inter: 
						inter = inter.intersection(helper(son))
					else: 
						inter = helper(son)
					union = union.union(helper(son))
			
				if inter:#is not empty
					node.R = inter
				else:
					node.R = union
				return node.R
			
		helper(tr.get_root())

	def r(self, node, tri ,trees):
		
		leaf = genetic_tree.is_leaf
			
		is_root = genetic_tree.is_root
		
		if leaf(node): 
			return
			
		elif node.r:
			
			for son in node.sons:
				self.r(son, tri, trees)
		
		elif is_root(node):
			
			for r_ in node.R:
				
				node.r = r_
				new_tree = tri.copy()
				trees.add(new_tree)
				self.r(new_tree.get_root(),new_tree, trees)
				
			trees.remove(tri)
		
		else:
			
			if node.father.r not in node.R:
				
				for r_ in node.R:
					
					node.r = r_
					new_tree = tri.copy()
					trees.add(new_tree)
					self.r(new_tree.get_root(),new_tree, trees)
				
				trees.remove(tri)
			
			else:
				
				node.r = node.father.r
				for son in node.sons:
					
					self.r(son, tri, trees)


if __name__ == '__main__':

	tr = genetic_tree()

	v1 = specie(name = 'v1')
	v2 = specie(name = 'v2')
	v3 = specie(name = 'v3')
	v4 = specie('AA', name = 'v4')
	v5 = specie('AC', name = 'v5')
	v6 = specie('CG', name = 'v6')
	v7 = specie('GC', name = 'v7')

	tr.root = v1

	tr.add_edge(v1, v2)
	tr.add_edge(v1, v3)

	tr.add_edge(v2, v4)
	tr.add_edge(v2, v5)

	tr.add_edge(v3, v6)
	tr.add_edge(v3, v7)
	
	tr2 = genetic_tree()

	v1 = specie(name = 'v1')
	v2 = specie(name = 'v2')
	v3 = specie(name = 'v3')
	v4 = specie('A', name = 'v4')
	v5 = specie('A', name = 'v5')
	v6 = specie('C', name = 'v6')
	v7 = specie('G', name = 'v7')

	tr2.root = v1

	tr2.add_edge(v1, v2)
	tr2.add_edge(v1, v3)

	tr2.add_edge(v2, v4)
	tr2.add_edge(v2, v5)

	tr2.add_edge(v3, v6)
	tr2.add_edge(v3, v7)

	fitch = fitch_tree(tr)
	
	fitch.R(tr2)
	
	s = set([tr2])
	fitch.r(tr2.get_root(), tr2, s)
	'''
	for tree in s:
		print tree


	for i in range(2):
		print i
		for trees in fitch.possible_r_trees:
			for tree in trees:	
				print tree

	'''
	
	list_of_options = [{'v1':'','v2':'','v3':'','v4':'','v5':'','v6':'','v7':''}]
	
	for i in range(2):
		
		new_list = []
		for place in list_of_options:
			
			for itree in fitch.possible_r_trees[i]:
			
				new_dic = dict(place)
				for node in itree.nodes:
					new_dic[node.name] += node.r
				new_list.append(new_dic)
				 
		list_of_options = new_list
			
	for list in list_of_options:
		print list
				
				
				
				
				
				
				