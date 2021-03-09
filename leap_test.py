import unittest
import leap_code

class test(unittest.TestCase):
	def test1(self):
		self.assertEqual(leap_code.leap(2004), "2004 is a leap year");

	def test2(self):
		self.assertEqual(leap_code.leap(2100), "2100 is not a leap year");

if __name__ == '__main__':
	unittest.main()
