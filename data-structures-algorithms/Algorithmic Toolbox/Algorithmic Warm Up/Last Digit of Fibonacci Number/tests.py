from test_helper import run_common_tests, failed, passed, check_tests_pass
from last_digit_of_fibonacci_number import last_digit_of_fibonacci_number


def fibonacci_number_last_digit_reference(n):
    assert 0 <= n <= 10 ** 6
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("last_digit_of_fibonacci_number_unit_tests.py")

    all_tests_passed = True
    for m in [2, 3, 239, 240, 1000, 9999, 10**6]:
        if last_digit_of_fibonacci_number(m) != fibonacci_number_last_digit_reference(m):
            all_tests_passed = False
            failed("Wrong answer for n={}".format(m))
            break

    if all_tests_passed:
        passed()
