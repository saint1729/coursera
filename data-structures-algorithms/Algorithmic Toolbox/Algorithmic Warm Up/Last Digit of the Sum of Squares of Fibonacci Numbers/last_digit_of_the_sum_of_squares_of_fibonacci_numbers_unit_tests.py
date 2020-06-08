import unittest
from last_digit_of_the_sum_of_squares_of_fibonacci_numbers import last_digit_of_the_sum_of_squares_of_fibonacci_numbers, last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive


class TestLastDigitOfTheSumOfSquaresOfFibonacciNumbers(unittest.TestCase):
    def test_small(self):
        for n in range(20):
            self.assertEqual(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n),
                             last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n))

    def test_large(self):
        for (n, last_digit) in [(73, 1), (1234567890, 0), type here]:
            self.assertEqual(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n), last_digit)


if __name__ == '__main__':
    unittest.main()
