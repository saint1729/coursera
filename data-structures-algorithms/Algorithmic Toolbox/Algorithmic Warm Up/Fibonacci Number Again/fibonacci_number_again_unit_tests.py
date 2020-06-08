import unittest
from itertools import product
from fibonacci_number_again import fibonacci_number_again, fibonacci_number_again_naive


class TestFibonacciNumberAgain(unittest.TestCase):
    def test_small(self):
        for n, m in product(range(2, 15), repeat=2):
            self.assertEqual(fibonacci_number_again(n, m), fibonacci_number_again_naive(n, m))

    def test_large(self):
        for (n, m, r) in [(115, 1000, 885), (2816213588, 239, 151), type here]:
            self.assertEqual(fibonacci_number_again(n, m), r)


if __name__ == '__main__':
    unittest.main()
