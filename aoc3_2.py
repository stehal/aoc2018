def readfile(name, fabric):
	f = {}
	for s in open(name):
		a = s.split('@')
		id = a[0]
		b = a[1].split(':')
		from_edge =  b[0].split(',')
		from_left = int(from_edge[0])
		from_top = int(from_edge[1])
		d= b[1].split('x')
		width = int(d[0])
		height = int(d[1])
		top_left = (from_left, from_top)
		bottom_right = (from_left+width, from_top+height)
		for x in range(top_left[0], bottom_right[0]):
			for y in range(top_left[1], bottom_right[1]):
				if fabric[x][y] == '.':
					fabric[x][y] =	 id
				else:
					fabric[x][y] = 'x'
		f[id]= (top_left, bottom_right)
	return fabric, f

def fabric(size):
	fabric = []
	for y in range(size):
		fabric.append( ['.'] * size)
	return fabric 

fabric, f = readfile('aoc3.txt', fabric(1000))

for key in f.keys():
	overlap = False
	value  = f[key]
	for x in range(value[0][0], value[1][0]):
		for y in range(value[0][1], value[1][1]):
			if fabric [x][y] != key:
				overlap = True	
	if not overlap:
		print("Resultat ", key)
		break
