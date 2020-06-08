from test_helper import run_common_tests, failed, passed, check_tests_pass
from number_of_inversions import compute_inversions, compute_inversions_naive
from random import randint


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("number_of_inversions_unit_tests.py")

    all_tests_passed = True
    for n in (3, 4, 5, 10, 100):
        for array in (
            [1] * n,
            [n - i for i in range(n)],
            [i for i in range(n)],
            [randint(0, n) for _ in range(n)]
        ):
            if compute_inversions(array) != compute_inversions_naive(array):
                all_tests_passed = False
                failed("Wrong answer for array={}".format(array))
                break

    if all_tests_passed:
        passed()
