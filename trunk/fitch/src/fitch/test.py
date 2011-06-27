from genetic_tree import *

tr = genetic_tree()

v1 = specie(name = 'v1')
v2 = specie(name = 'v2')
v3 = specie(name = 'v3')
v4 = specie('A', name = 'v4')
v5 = specie('A', name = 'v5')
v6 = specie('A', name = 'v6')
v7 = specie('G', name = 'v7')

tr.add_edge(v1, v2)
tr.add_edge(v1, v3)
tr.add_edge(v2, v4)
tr.add_edge(v2, v5)

tr.root = v1
tr.add_edge(v3, v6)
tr.add_edge(v3, v7)

v =  tr.get_node(tr.by_name('v1'))
print type(v)
print v.R

def ni(x):
	print x
	if x < 0: 
		print 'done'
		return
	ni(x-1)
	
	
ni(5)

