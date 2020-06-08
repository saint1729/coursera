from test_helper import run_common_tests, failed, passed, check_tests_pass
from organizing_lottery import points_cover, points_cover_naive
from random import randint


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("organizing_lottery_unit_tests.py")

    all_tests_passed = True

    for n in (3, 4, 5, 10, 100):
        for m in (3, 4, 100, 200):
            points = [randint(-10, 10) for _ in range(m)]
            starts = [randint(-5, 0) for _ in range(n)]
            ends = [randint(0, 5) for _ in range(n)]

            if points_cover(starts, ends, points) != points_cover_naive(starts, ends, points):
                all_tests_passed = False
                failed("Wrong answer for starts={}, ends={}, points={}".format(starts, ends, points))
                break

    if all_tests_passed:
        passed()
