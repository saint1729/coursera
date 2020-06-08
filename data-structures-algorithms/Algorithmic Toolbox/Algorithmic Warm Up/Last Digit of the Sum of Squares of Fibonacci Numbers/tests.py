from test_helper import run_common_tests, failed, passed, check_tests_pass
from last_digit_of_the_sum_of_squares_of_fibonacci_numbers import last_digit_of_the_sum_of_squares_of_fibonacci_numbers


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("last_digit_of_the_sum_of_fibonacci_numbers_unit_tests.py")

    all_tests_passed = True
    for n, d in [(73, 1)]:
        if last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n) != d:
            all_tests_passed = False
            failed("Wrong answer for n={}".format(n))
            break

    if all_tests_passed:
        passed()
