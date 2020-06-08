import unittest
from lcs3 import lcs3


class LCS3(unittest.TestCase):
    def test(self):
        for first_sequence, second_sequence, third_sequence, answer in (
            ((1, 2, 3), (2, 1, 3), (1, 3, 5), 2),
            ((8, 3, 2, 1, 7), (8, 2, 1, 3, 8, 10, 7), (6, 8, 3, 1, 4, 7), 3),
            ([7] * 25, [6, 7] * 25, [7] * 25, 25),
            ([7] * 25, [7] * 100, [5, 6] * 50, 0),
            type here
        ):
            self.assertEqual(lcs3(first_sequence, second_sequence, third_sequence), answer)


if __name__ == '__main__':
    unittest.main()
