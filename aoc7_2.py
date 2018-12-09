import string
from collections import defaultdict

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

completed = []
plus = 60
worker_available = ["W1","W2","W3","W4","W5"]
working = {}
work_available = start
work_available.sort()
while work_available and worker_available:
	w = work_available.pop(0)
	worker = worker_available.pop(0)
	working[w] = [string.ascii_uppercase.index(w) + 1 + plus, 1, worker]

total_time = 0
k =0

while (len(work_available) > 0 or len(working) > 0) :
	completed_work = []
	
	for work, t in working.items():
		if t[0] == t[1] :
			completed.append(work)
			completed_work.append(work)
			worker_available.append(t[2])
		t[1] += 1
	for c in completed_work :
		working.pop(c, None)
		for n in forward[c]:
			if n not in work_available:
				if set( backward[n]).issubset(set(completed)): 
					work_available.append(n)
					
		work_available.sort()
		
	while work_available and worker_available:
		w = work_available.pop(0)
		worker = worker_available.pop(0)
		working[w] = [string.ascii_uppercase.index(w) + 1 + plus, 1, worker]
	
	total_time += 1
print(total_time)
	
	
	
