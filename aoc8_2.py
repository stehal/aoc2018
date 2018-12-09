tree = list(map(int, open('aoc8.txt').read().split()))
node = 0
entries = []

def readtree(tree, node, entries):
	meta = tree[:2]
	
	countchildren = meta[0]
	countmeta = meta[1]
	
	tree = tree[2:]
	children = []
	if countchildren == 0:
		return tree[countmeta:], sum(tree[:countmeta])
	for child in range(countchildren):
		node +=1
		tree, s = readtree(tree, node, entries)
		children.append(s)
		
	entries = tree[:countmeta]
	sumt = 0
	for e in entries:
		if e <= len(children):
			sumt += children[e-1]
		
	tree = tree[countmeta:]
	return tree,  sumt
	
t,s = readtree(tree, node, entries)
print(s)

		