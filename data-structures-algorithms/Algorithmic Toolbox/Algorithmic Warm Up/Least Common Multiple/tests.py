import math
from random import randint
from test_helper import run_common_tests, failed, passed, check_tests_pass
from lcm import lcm

if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("lcm_unit_tests.py")

    all_tests_passed = True
    for _ in range(10):
        a, b = randint(1, 10 ** 18), randint(1, 10 ** 18)
        if lcm(a, b) != a * b // math.gcd(a, b):
            all_tests_passed = False
            failed("Wrong answer for a={}, b={}".format(a, b))
            break

        c = randint(1, 10 ** 9)
        a, b = randint(1, 10 ** 9) * c, randint(1, 10 ** 9) * c
        if lcm(a, b) != a * b // math.gcd(a, b):
            all_tests_passed = False
            failed("Wrong answer for a={}, b={}".format(a, b))
            break

    if all_tests_passed:
        passed()
