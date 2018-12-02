from collections import defaultdict
threes = 0
twos = 0
for s in open('aoc2.txt'):
	three = 0
	two = 0
	d = {}
	d = defaultdict(lambda:0,d)
	for a in s.rstrip('\r\n'):
		d[a] = d[a] + 1
	for key, value in d.items():
		if value == 2:
			two = 1
		if value == 3:
			three = 1
	threes += three
	twos += two
print(threes*twos)
	
		