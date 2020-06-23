import unittest
from closest_points import minimum_distance_squared, minimum_distance_squared_naive, Point
from random import randint


class ClosestPoints(unittest.TestCase):
    def test_small(self):
        for points in (
            [Point(1, 0), Point(1, 1)],
            [Point(-1, -3), Point(0, 0), Point(-3, 1), Point(1, -3), Point(-1, 3)]
        ):
            actual_answer = minimum_distance_squared(points)
            expected_answer = minimum_distance_squared_naive(points)
            self.assertAlmostEqual(actual_answer,
                                   expected_answer,
                                   delta=1e-03)

    def test_random(self):
        for n in [2, 5, 10, 100]:
            for max_value in [1, 2, 3, 1000]:
                points = []
                for _ in range(n):
                    x = randint(-max_value, max_value)
                    y = randint(-max_value, max_value)
                    points.append(Point(x, y))
                points2 = points[:]
                actual_value = minimum_distance_squared(points)
                expected_value = minimum_distance_squared_naive(points)
                self.assertAlmostEqual(actual_value,
                                       expected_value,
                                       delta=1e-03)

    def test_large(self):
        self.test_small()


if __name__ == '__main__':
    unittest.main()
