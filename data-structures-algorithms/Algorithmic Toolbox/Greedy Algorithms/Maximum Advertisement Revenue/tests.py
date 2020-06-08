from random import randint
from test_helper import run_common_tests, failed, passed, check_tests_pass
from maximum_ad_revenue import max_dot_product


def reference(a, b):
    a = sorted(a)
    b = sorted(b)
    return sum(a[i] * b[i] for i in range(len(a)))


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("maximum_ad_revenue_unit_tests.py")

    all_tests_passed = True

    for n in [10, 20, 30]:
        a = [randint(0, 10 ** 5) for _ in range(n)]
        b = [randint(0, 10 ** 5) for _ in range(n)]

        if reference(a, b) != max_dot_product(a, b):
            all_tests_passed = False
            failed("Wrong answer for a={}, b={}".format(a, b))

    if all_tests_passed:
        passed()
