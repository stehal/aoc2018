import unittest

def remove(s):
	ss = '.'
	for c in s:
		previous = ss[-1]
		if previous != c and c.upper() == previous.upper():
			ss = ss[:-1]
		else:
			ss += c
	return ss[1:]

class TestStringMethods(unittest.TestCase):
	
	def test(self):
		self.assertEqual( remove('aA'), '')
		self.assertEqual( remove('abBA'), '')
		self.assertEqual( remove('abAB'), 'abAB')
		self.assertEqual( remove('aabAAB'), 'aabAAB')
		self.assertEqual( remove('dabAcCaCBAcCcaDA'), 'dabCBAcaDA')
	
#if __name__ == '__main__':
#   unittest.main()

with open('aoc5.txt') as f:
	print("Result", len(remove(f.read())))