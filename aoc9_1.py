import unittest
	
class TestMethods(unittest.TestCase):
	def testPos(self):
		self.assertEqual(pos(0, 1), 1)
		self.assertEqual(pos(1, 2), 1)
		self.assertEqual(pos(1, 3), 3)
		self.assertEqual(pos(3, 4), 1)
		self.assertEqual(pos(1, 5), 3)

def pos(current, length):
	if current + 2 > length:
		return 1
	return current + 2

last_marble=72170
circle = [0] #list
current = 0
no_elfs = 470
elfs = [0] * no_elfs

for m in range(1,last_marble + 1):
	if m % 23 == 0:
		if current - 7 < 0:
			index = len(circle) + (current -7)
		else:
			index = current - 7
		elfs[(m % no_elfs) -1] += m + (circle[index])
		del circle[index]
		current = index
	else:
		ins = pos(current,len(circle))	
		circle.insert(ins, m)
		current = ins
	
print(max(elfs))
