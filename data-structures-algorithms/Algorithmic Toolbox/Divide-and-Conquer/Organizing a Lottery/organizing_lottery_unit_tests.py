import unittest
from organizing_lottery import points_cover, points_cover_naive


class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            # ([0, 7], [5, 10], [1, 6, 11]),
            # ([4, 2], [10, 6], [5, 8, 3]),
            ([3, 3], [4, 4], [3, 3])
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_random(self):
        for starts, ends, points in [
            ([9, 10, 11, 2, 3], [30, 40, 16, 4, 5], [7, 2, 13, 15, 10, 33, 19])
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_large(self):
        self.test_small()


if __name__ == '__main__':
    unittest.main()
