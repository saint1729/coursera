from test_helper import run_common_tests, failed, passed, check_tests_pass
from fibonacci_number_again import fibonacci_number_again


def pisano_period(m):
    current, next = 0, 1
    period = 0

    while True:
        current, next = next, (current + next) % m
        period += 1
        if current == 0 and next == 1:
            return period


def fib_mod(n, m):
    current, next = 0, 1
    for _ in range(n):
        current, next = next, (current + next) % m

    return current


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("fibonacci_number_again_unit_tests.py")

    all_tests_passed = True
    for (n, m) in [(7, 239), (239, 7), (10 ** 18, 239)]:
        if fibonacci_number_again(n, m) != fib_mod(n % pisano_period(m), m):
            all_tests_passed = False
            failed("Wrong answer for n={}".format(m))
            break

    if all_tests_passed:
        passed()
