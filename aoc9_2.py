last_marble=7217000
no_elfs = 470
elfs = []
circle = {0:[0, 0]} #double linked list
current = 0
no_elfs = 470
elfs = [0] * no_elfs
for m in range(1,last_marble + 1):

	if m % 23 == 0:
		previous = previous = circle[m-1][0]
		for i in range(6):
			previous = circle[previous][0]
		elfs[(m % no_elfs) -1] += previous + m
		
		previousprevious=circle[previous][0]
		current = circle[previous][1]
		
		circle[previousprevious][1] = current
		circle.pop(m, None)
		circle[current][0] = previousprevious
		
	else:
		next = circle[current][1]
		nextnext = circle[next][1]
		circle[next][1] = m
		circle[nextnext][0] = m
		circle[m] = [next, nextnext]
		current = m

print(max(elfs))
