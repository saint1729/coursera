import math
from test_helper import run_common_tests, failed, passed, check_tests_pass
from gcd import gcd

if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("gcd_unit_tests.py")

    all_tests_passed = True
    for (a, b) in [(2, 3), (10**8, 10**5 - 1), (10**8, 10**9)]:
        if gcd(a, b) != math.gcd(a, b):
            all_tests_passed = False
            failed("Wrong answer for a={}, b={}".format(a, b))
            break

    if all_tests_passed:
        passed()
