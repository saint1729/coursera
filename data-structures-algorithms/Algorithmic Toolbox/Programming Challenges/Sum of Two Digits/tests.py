from test_helper import run_common_tests, failed, passed, check_tests_pass
from itertools import product
from sum_of_two_digits import sum_of_two_digits

if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("sum_of_two_digits_unit_tests.py")

    all_tests_passed = True
    for a, b in product(range(10), repeat=2):
        if sum_of_two_digits(a, b) != a + b:
            all_tests_passed = False
            failed("Wrong answer for a={}, b={}".format(a, b))
            break

    if all_tests_passed:
        passed()
