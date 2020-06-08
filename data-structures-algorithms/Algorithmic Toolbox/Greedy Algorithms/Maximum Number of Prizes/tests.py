from test_helper import run_common_tests, failed, passed, check_tests_pass
from maximum_number_of_prizes import compute_optimal_summands


def reference(n):
    summands = []

    k = 1
    while n >= k + k + 1:
        summands.append(k)
        n -= k
        k += 1
    summands.append(n)

    return summands


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("maximum_number_of_prizes_unit_tests.py")

    all_tests_passed = True
    for n in [2, 7, 20, 239, 317]:
        if reference(n) != compute_optimal_summands(n):
            all_tests_passed = False
            failed("Wrong answer for n={}".format(n))
            break

    if all_tests_passed:
        passed()
