all = set()
for s in open('aoc2.txt'):
	all.add(s)
	
	for b in all:
		diffs = 0
		for c, d in zip(b, s):
			if c!= d:
				diffs += 1
		if diffs == 1:
			out = ''
			for p, q in zip(s,b):
				if p==q:
					out += p
			print(out)
			