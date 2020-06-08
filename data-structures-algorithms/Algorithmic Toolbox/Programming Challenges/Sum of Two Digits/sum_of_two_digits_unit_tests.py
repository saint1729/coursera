import unittest
from itertools import product
from sum_of_two_digits import sum_of_two_digits


class TestSumOfTwoDigits(unittest.TestCase):
    def test_all_inputs(self):
        for first_digit, second_digit in product(range(10), repeat=2):
            self.assertEqual(sum_of_two_digits(first_digit, second_digit), first_digit + second_digit)


if __name__ == '__main__':
    unittest.main()
