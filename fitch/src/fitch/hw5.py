from fitch import *

if __name__ == '__main__':    
    
    print 'a)'

    tr = genetic_tree()

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

    fitch = fitch_tree(tr)
    

    for list in fitch.possible_trees:
        line = ''
        for name, letter in  list.items():
            line += name+': '+letter+', '
        print line[:-2]

    print 'b)'

    tr = genetic_tree()

    v1 = specie(name = 'v1')
    v2 = specie(name = 'v2')
    v3 = specie(name = 'v3')
    v4 = specie('GA', name = 'v4')
    print v4.name+':', v4.r
    v5 = specie('AC', name = 'v5')
    print v5.name+':', v5.r
    v6 = specie('AG', name = 'v6')
    print v6.name+':', v6.r
    v7 = specie('CA', name = 'v7')
    print v7.name+':', v7.r

    tr.root = v1

    tr.add_edge(v1, v2)
    tr.add_edge(v1, v3)

    tr.add_edge(v2, v4)
    tr.add_edge(v2, v5)

    tr.add_edge(v3, v6)
    tr.add_edge(v3, v7)

    fitch = fitch_tree(tr)
    
    for tree in fitch.possible_trees:
        line = ''
        for name, r in tree.items():
            line += name+': '+ r +', '
        print line[:-2]
    
    
    print 'c)'
    
    tr = genetic_tree()

    v1 = specie(name = 'v1')
    v2 = specie(name = 'v2')
    v3 = specie(name = 'v3')
    v4 = specie('AA', name = 'v4')
    print v4.name+':', v4.r
    v5 = specie('GA', name = 'v5')
    print v5.name+':', v5.r
    v6 = specie('CA', name = 'v6')
    print v6.name+':', v6.r
    v7 = specie('TA', name = 'v7')
    print v7.name+':', v7.r

    tr.root = v1

    tr.add_edge(v1, v2)
    tr.add_edge(v1, v3)

    tr.add_edge(v2, v4)
    tr.add_edge(v2, v5)

    tr.add_edge(v3, v6)
    tr.add_edge(v3, v7)

    fitch = fitch_tree(tr)
    
    non_fitch = {'v1':'CA', 'v2':'CA', 'v3':'CA', 'v4':'AA', 'v5':'GA', 'v6': 'CA', 'v7':'TA', }
    
    for list in fitch.possible_trees:
        line = ''
        #print line
        
        for name, letter in  list.items():
            line += name+': '+letter+', '
        print line[:-2]
    
    print 'these are all fitch assignments.'
    print 'and their most parsimony score is', str(fitch.score)+'.'
    print 'another assignment is:'
    line = ''
    for name, letter in  non_fitch.items():
            line += name+': '+letter+', '
    print line[:-2]
    
    print 'd)'

    tr = genetic_tree()

    v1 = specie(name = 'v1')
    v2 = specie(name = 'v2')
    v3 = specie(name = 'v3')
    v4 = specie('AAAG', name = 'v4')
    print v4.name+':', v4.r
    v5 = specie('AAGA', name = 'v5')
    print v5.name+':', v5.r
    v6 = specie('AGAA', name = 'v6')
    print v6.name+':', v6.r
    v7 = specie('GAAA', name = 'v7')
    print v7.name+':', v7.r

    tr.root = v1

    tr.add_edge(v1, v2)
    tr.add_edge(v1, v3)

    tr.add_edge(v2, v4)
    tr.add_edge(v2, v5)

    tr.add_edge(v3, v6)
    tr.add_edge(v3, v7)
    
    fitch = fitch_tree(tr)
    
    for list in fitch.possible_trees:
        line = ''
    
        for name, letter in  list.items():
            line += name+': '+letter+', '
        print line[:-2]
