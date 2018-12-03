def readfile(name, fabric):
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
					fabric[x][y] = id
				else:
					fabric[x][y] = 'x'
	return fabric

def fabric(size):
	fabric = []
	for y in range(size):
		fabric.append( ['.'] * size)
	return fabric 

count=0
for a in readfile('aoc3.txt', fabric(1000)):
	for b in a:
		if b == 'x':
			count +=1
			
print("Result ", count)
