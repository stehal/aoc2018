
t = 0
a = {0}
b = True
while b:
	for s in open('aoc1.txt'):
		n = int(s)
		t += n
		if t in a:
			print(t)
			b= False
			break
		a.add(t)
		

