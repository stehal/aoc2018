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
	
def remove_poly(s, c):
	ss = ""
	for char in s:
		if char.lower() != c:
			ss += char
	return ss
	


class TestStringMethods(unittest.TestCase):
	
	def test(self):
		self.assertEqual( remove('aA'), '')
		self.assertEqual( remove('abBA'), '')
		self.assertEqual( remove('abAB'), 'abAB')
		self.assertEqual( remove('aabAAB'), 'aabAAB')
		self.assertEqual( remove('dabAcCaCBAcCcaDA'), 'dabCBAcaDA')
	def test_remove(self):
		self.assertEqual( remove_poly('dabAcCaCBAcCcaDA', 'c'), 'dabAaBAaDA')
		
		
	
#if __name__ == '__main__':
#    unittest.main()

with open('aoc5.txt') as f:
	ss = f.read()
	length = len(ss) 

	for char in 'abcdefghijklmnopqrstuvwxyz':
		sss = remove_poly(ss, char)
		ssss = remove(sss)
		if len(ssss) < length:
			length = len(ssss)
			
		
	print("Result", length)
	