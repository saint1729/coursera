import unittest
from lcs2 import lcs2


class LCS2(unittest.TestCase):
    def test(self):
        for first_sequence, second_sequence, answer in (
            ((1, 2), (2, 1), 1),
            ((1, 2), (3, 4), 0),
            ([17] * 50, [17] * 25, 25),
            ([1] * 100, [1] * 100, 100),
            ((2, 7, 5), (2, 5), 2),
            ((7, ), (1, 2, 3, 4), 0),
            ((2, 7, 8, 3), (5, 2, 8, 7), 2),
            type here
        ):
            self.assertEqual(lcs2(first_sequence, second_sequence), answer)


if __name__ == '__main__':
    unittest.main()
