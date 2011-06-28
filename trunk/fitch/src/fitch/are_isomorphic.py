from graph.genetic_tree import genetic_tree as tree
from graph.genetic_tree import specie
is_leaf = tree.is_leaf

'''
Q4
'''

def are_isomorphic(tree1, tree2):
    
    def dosomorphic(node1, node2):
        
        # leaf(node1) XOR leaf(node2)
        if is_leaf(node1) and not is_leaf(node2) or not is_leaf(node1) and is_leaf(node2) or len(node1.sons) != len(node2.sons):
            return False
         
        elif is_leaf(node1) and is_leaf(node2):
            
            if node1.name == node2.name:
                return True
            return False
        
        else: 
            if len(node1.sons)  == 2:
                return dosomorphic(node1.sons[0], node2.sons[0]) and dosomorphic(node1.sons[1], node2.sons[1]) \
                    or dosomorphic(node1.sons[0], node2.sons[1]) and dosomorphic(node1.sons[1], node2.sons[0]) 
            else:
                
                return dosomorphic(node1.sons[0], node2.sons[1])
            
    return dosomorphic(tree1.get_root(), tree2.get_root())

if __name__ == '__main__':
    
    tr = tree()

    v1 = specie(name = 'v1')
    v2 = specie(name = 'v2')
    v3 = specie(name = 'v3')
    v4 = specie('AA', name = 'v4')
    print 'v4: AA'
    v5 = specie('AC', name = 'v5')
    print 'v5: AC'
    v6 = specie('CG', name = 'v6')
    print 'v6: CG'
    v7 = specie('GC', name = 'v7')
    print 'v4: GC'

    tr.root = v1

    tr.add_edge(v1, v2)
    tr.add_edge(v1, v3)

    tr.add_edge(v2, v4)
    tr.add_edge(v2, v5)

    tr.add_edge(v3, v6)
    tr.add_edge(v3, v7)

    tr2 = tree()

    v1 = specie(name = 'v1')
    v2 = specie(name = 'v2')
    v3 = specie(name = 'v')
    v4 = specie('GA', name = 'a')
    print v4.name+':', v4.r
    v5 = specie('AC', name = 'b')
    print v5.name+':', v5.r
    v6 = specie('AG', name = 'c')
    print v6.name+':', v6.r
    v7 = specie('CA', name = 'v7')
    print v7.name+':', v7.r

    tr2.root = v1

    tr2.add_edge(v1, v2)
    tr2.add_edge(v1, v3)

    tr2.add_edge(v2, v4)
    tr2.add_edge(v2, v5)

    tr2.add_edge(v3, v6)
    tr2.add_edge(v3, v7)
    
    print are_isomorphic(tr, tr2)