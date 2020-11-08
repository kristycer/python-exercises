import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

	def test_simple_returns_the_number(self):
		self.assertEqual(FizzBuzz(1), 1)
		self.assertEqual(FizzBuzz(2), 2)
		self.assertEqual(FizzBuzz(4), 4)

	def test_multiples_of_3_return_fizz(self):
		self.assertEqual(FizzBuzz(3), "fizz")
		self.assertEqual(FizzBuzz(6), "fizz")

	
		

if __name__ == '__main__':
	unittest.main()