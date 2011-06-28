from graph.genetic_tree import genetic_tree 
from graph.genetic_tree import specie
from graph.tree import tree


class fitch_tree(tree):
	
	def __init__(self, tr):
		
		self.gtr = tr
		self.possible_r_trees = []
		self.possible_trees = []
		self.len = len(self.gtr.get_leaf().r)
		self.score = 0
		
		for i in range(self.len):

			index_tree = self.gtr.copy()
			for node in index_tree.nodes:

				if node.r: 

					node.r = node.r[i]
					node.R = set([node.r])

			self.R(index_tree)
			self.possible_r_trees.append(set([index_tree]))
			self.r(index_tree.get_root(),index_tree, self.possible_r_trees[i])
		self.get_possible_trees()
		
	def get_possible_trees(self):
		
		self.names = []
		for node in self.gtr.nodes:
			self.names.append(node.name)
		
		dic = {}
		for name in self.names:
			dic[name] = ''
		
		self.possible_trees.append(dic)
	
		
		for i in range(self.len):
			
			new_list = []
			for place in self.possible_trees:
				
				for itree in self.possible_r_trees[i]:
				
					new_dic = dict(place)
					for node in itree.nodes:
						new_dic[node.name] += node.r
					new_list.append(new_dic)
					 
			self.possible_trees = new_list

	def R(self, tr):
		tr.score = 0
		def helper(node):
			
			if node.R: 
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
					self.score += 1
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
	v4 = specie('A', name = 'v4')
	v5 = specie('C', name = 'v5')
	v6 = specie('G', name = 'v6')
	v7 = specie('T', name = 'v7')

	tr.root = v1

	tr.add_edge(v1, v2)
	tr.add_edge(v1, v3)

	tr.add_edge(v2, v4)
	tr.add_edge(v2, v5)

	tr.add_edge(v3, v6)
	tr.add_edge(v3, v7)

	fitch = fitch_tree(tr)
	
	for tree in fitch.possible_trees:
		print tree
	
	print 'fitch.score', fitch.score

    

