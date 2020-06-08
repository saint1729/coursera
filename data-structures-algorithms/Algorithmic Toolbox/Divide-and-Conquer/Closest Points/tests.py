from test_helper import run_common_tests, failed, passed, check_tests_pass
from closest_points import minimum_distance_squared, minimum_distance_squared_naive, Point
from math import fabs
from random import randint


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("closest_points_unit_tests.py")

    all_tests_passed = True

    for points in (
        [Point(-10 ** 9, - 10 ** 9), Point(10 ** 9, 10 ** 9)],
        [Point(i, i + 1) for i in range(100)],
        [Point(randint(1, 10), randint(1, 10)) for _ in range(5)],
        [Point(randint(1, 10), randint(1, 10)) for _ in range(500)]
    ):
        if fabs(minimum_distance_squared(points) - minimum_distance_squared_naive(points)) > 1e-03:
            all_tests_passed = False
            failed("Wrong answer for points={}".format(points))
            break

    if all_tests_passed:
        passed()
