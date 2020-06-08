import unittest
from maximum_gold import maximum_gold


class MaximumGold(unittest.TestCase):
    def test(self):
        for capacity, weights, answer in (
            (10, (1, 4, 8), 9),
            (20, (5, 7, 12, 18), 19),
            (10, (3, 5, 3, 3, 5), 10),
            type here
        ):
            self.assertEqual(maximum_gold(capacity, weights), answer)


if __name__ == '__main__':
    unittest.main()
