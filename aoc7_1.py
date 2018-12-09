from collections import defaultdict


def next(starts, forward, backward, path):
	for s in starts:
		if s in path:
			return path
		path.append(s)
		
		list_n = forward[s]
		list_n.sort()
		for n in list_n:
			if set( backward[n]).issubset(set(path)): 
				next([n], forward, backward, path)
	return path
	
	

forward = defaultdict(lambda:[])
backward = defaultdict(lambda:[])
all = set()
with open('aoc7.txt') as f:
	for line in f.readlines():
		finished= line[5]
		before = line[36]
		forward[finished].append(before) 
		backward[before].append(finished)
		all.add(before)
		all.add(finished)
all_befores = backward.keys()
start = []
for a in all:
	if a not in all_befores:
		start.append(a)

		
start.sort()
print(''.join(next(start, forward, backward, [])))
