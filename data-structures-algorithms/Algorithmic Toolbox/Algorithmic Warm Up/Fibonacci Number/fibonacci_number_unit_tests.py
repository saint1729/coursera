import unittest
from fibonacci_number import fibonacci_number, fibonacci_number_naive


class TestFibonacciNumber(unittest.TestCase):
    def test_small(self):
        for n in range(8):
            self.assertEqual(fibonacci_number(n), fibonacci_number_naive(n))

    def test_large(self):
        for (n, Fn) in [(30, 832040), (35, type here), (40, 102334155)]:
            self.assertEqual(fibonacci_number(n), Fn)


if __name__ == '__main__':
    unittest.main()
