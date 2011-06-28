from fitch import fitch_tree
from graph.genetic_tree import specie, genetic_tree 


alpabet = ['A','C','T','G']

class aml_tree(fitch_tree):
    
    def __init__(self):
        pass
    
    def R(self, tr):
        
        def helper(node):
            
            if node.r: 
                node.R = {}
                for letter in alpabet:
                    node.R[letter] = 0
                node.R[node.r] = 1 
                return 
            
            else:
                for son in node.sons:
                    helper(son)
                 
                node.R = {'A':0,'C':0,'T':0,'G':0}
                
                for letter1 in alpabet:
                    
                    val1 = 0
                    for letter2 in alpabet:
                        val = node.theta[letter1][letter2]
                        val *=  node.sons[0].R[letter2]
                        if val >= val1: val1 = val
                    
                    val2 = 0
                    for letter2 in alpabet:
                        val = node.theta[letter1][letter2]
                        val *= node.sons[1].R[letter2]
                        if val >= val2: val2 = val
                    
                    node.R[letter1] = val1 + val2
            
            return        
        print 'going to helper'
        helper(tr.get_root())

if __name__ == '__main__':
    
    theta = {'A':{'A':0.4,'C':0.4,'G':0.1,'T':0.1},'C':{'A':0.4,'C':0.4,'G':0.1,'T':0.1},'G':{'A':0.4,'C':0.4,'G':0.1,'T':0.1},'T':{'A':0.4,'C':0.4,'G':0.1,'T':0.1}}
    
    tr = genetic_tree()

    v1 = specie(name = 'v1', theta = theta)
    v2 = specie(name = 'v2', theta = theta)
    v3 = specie(name = 'v3', theta = theta)
    v4 = specie('A', name = 'v4', theta = theta)
    v5 = specie('C', name = 'v5', theta = theta)
    v6 = specie('G', name = 'v6', theta = theta)
    v7 = specie('T', name = 'v7', theta = theta)
    
    print v7.theta

    tr.root = v1

    tr.add_edge(v1, v2)
    tr.add_edge(v1, v3)

    tr.add_edge(v2, v4)
    tr.add_edge(v2, v5)

    tr.add_edge(v3, v6)
    tr.add_edge(v3, v7)

    aml = aml_tree()
    
    print 'not in __init'
    print aml.R(tr)
    print tr.get_root().R
    for node in tr.nodes:
        print node.name, node.R
    