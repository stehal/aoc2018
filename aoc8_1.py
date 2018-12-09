import unittest

tree = list(map(int, open('aoc8.txt').read().split()))

for d in ss:
	tree.append(int(d))

node = 0
entries = []
def readtree(tree, node, entries):
	meta = tree[:2]
	
	countchildren = meta[0]
	countmeta = meta[1]
	
	tree = tree[2:]
	
	for child in range(countchildren):
		node +=1
		tree = readtree(tree, node, entries)
		
	entries += tree[:countmeta]
	tree = tree[countmeta:]
	return tree
	
	
	
readtree(tree, node, entries)
print(sum(entries))

		