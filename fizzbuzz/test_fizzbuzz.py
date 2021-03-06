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

        def test_multiple_of_5_return_buzz(self):
		self.assertEqual(FizzBuzz(5), "buzz")
		self.assertEqual(FizzBuzz(10), "buzz")

        def test_multiple_of_15_return_fizzbuzz(self):
		self.assertEqual(FizzBuzz(60), "fizzbuzz")
		self.assertEqual(FizzBuzz(15), "fizzbuzz")

        # def test_it_has_range(self):
		# self.assertEqual(FizzBuzz(110), "Not allowed")
	

    

	
		

if __name__ == '__main__':
	unittest.main()