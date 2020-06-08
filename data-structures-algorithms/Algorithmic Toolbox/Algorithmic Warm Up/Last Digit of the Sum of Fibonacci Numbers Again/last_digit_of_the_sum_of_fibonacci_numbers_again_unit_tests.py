import unittest
from itertools import combinations
from last_digit_of_the_sum_of_fibonacci_numbers_again import last_digit_of_the_sum_of_fibonacci_numbers_again, \
    last_digit_of_the_sum_of_fibonacci_numbers_again_naive


class TestLastDigitOfTheSumOfFibonacciNumbersAgain(unittest.TestCase):
    def test_small(self):
        for from_index, to_index in combinations(range(2, 15), 2):
            self.assertEqual(last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index),
                             last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index))

    def test_large(self):
        for (from_index, to_index, last_digit) in [(3, 7, 1), (10, 10, 5), (100, 200, 0),
                                                   (17, 1700, 7),
                                                   (19, 10000000000, 1),
                                                   type here]:
            self.assertEqual(last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index), last_digit)


if __name__ == '__main__':
    unittest.main()
