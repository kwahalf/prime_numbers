""" Tests our prime number function """

import unittest
from prime_numbers import prime_numbers


class TestPrimeNumbers(unittest.TestCase):
    """ Tests prime_numbers functionality """

    def test_input_is_positive(self):
        self.assertEqual(prime_numbers(-5), [])
    def test_input_is_Not_a_list(self):
    	self.assertRaises(TypeError,prime_numbers, [2,4])
    def test_input_is_zero(self):
        self.assertEqual(prime_numbers(0), [])
    def test_output_is_primeNumbers(self):
        self.assertEqual(prime_numbers(8), [1,2,3,5,7])
    def test_input_is_not_a_dictionary(self):
        self.assertRaises(TypeError,prime_numbers, {"jane":2, "tom":4})
if __name__ == "__main__":
    unittest.main(exit = False)