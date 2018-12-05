from collections import defaultdict

def readfile(name):
	with open(name) as f:
		lines = f.read().splitlines()
		lines.sort()
	return lines

	
	
lines = readfile('aoc4.txt')
			
id = ''
start = 0

d = {}
e = {}
			
for line in lines:
	min = line[15:17]
	type = line[19] 
	if type == 'G':
		id = int(line.split('#')[1].split()[0])
	
	elif type == 'f':
		start = int(min)
	elif type == 'w':
		
		end = int(min)
		if not id in e.keys():
			e[id] = end -start
		else:
			e[id] += (end -start)
		for m in range(start,end):
			if not id in d.keys():
				d[id] = {m:1}
			else:
				if not m in d[id].keys():
					d[id][m] = 1
				else:
					d[id][m] += 1
max = 0
g = 0					
for k in e.keys():
	if e[k] > max:
		max = e[k]
		g=k
		
maxmin =0

h = ''
for k in d[g]:
	if d[g][k] > maxmin:
		maxmin = d[g][k]
		h = k
print(g*h)	

		
		
		
	
