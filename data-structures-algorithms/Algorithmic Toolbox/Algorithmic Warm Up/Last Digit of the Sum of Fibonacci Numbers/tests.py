from test_helper import run_common_tests, failed, passed, check_tests_pass
from last_digit_of_the_sum_of_fibonacci_numbers import last_digit_of_the_sum_of_fibonacci_numbers


def fibonacci_sum_last_digit(n):
    n = (n + 2) % 60

    prev, cur = 0, 1
    for _ in range(n):
        prev, cur = cur, (prev + cur) % 10

    return (prev + 9) % 10


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("last_digit_of_the_sum_of_fibonacci_numbers_unit_tests.py")

    all_tests_passed = True
    for n in [2, 3, 239, 240, 1000, 9999, 10 ** 17]:
        if last_digit_of_the_sum_of_fibonacci_numbers(n) != fibonacci_sum_last_digit(n):
            all_tests_passed = False
            failed("Wrong answer for n={}".format(n))
            break

    if all_tests_passed:
        passed()
