import unittest
from itertools import product
from lcm import lcm, lcm_naive


class TestLCM(unittest.TestCase):
    def test_small(self):
        for (a, b) in product(range(1, 15), repeat=2):
            self.assertEqual(lcm(a, b), lcm_naive(a, b))

    def test_large(self):
        for (a, b, m) in [(28851538, 1183019, 1933053046), type here]:
            self.assertEqual(lcm(a, b), m)


if __name__ == '__main__':
    unittest.main()
