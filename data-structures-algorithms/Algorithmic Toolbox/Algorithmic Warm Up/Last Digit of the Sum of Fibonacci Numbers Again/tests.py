from test_helper import run_common_tests, failed, passed, check_tests_pass
from last_digit_of_the_sum_of_fibonacci_numbers_again import last_digit_of_the_sum_of_fibonacci_numbers_again


def fibonacci_sum_last_digit(n):
    n = n % 60

    prev, cur = 0, 1
    for _ in range(n):
        prev, cur = cur, (prev + cur) % 10

    return (prev + 9) % 10

def reference(from_index, to_index):
    return (20 + fibonacci_sum_last_digit(to_index + 2) - fibonacci_sum_last_digit(from_index + 1)) % 10


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("last_digit_of_the_sum_of_fibonacci_numbers_again_unit_tests.py")

    all_tests_passed = True
    for (from_index, to_index) in [(1, 2), (2, 239), (1, 10 ** 10), (10 ** 10, 10 ** 13)]:
        assert from_index <= to_index
        if last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index) != reference(from_index, to_index):
            all_tests_passed = False
            failed("Wrong answer for m={}, n={}: {} {}".format(from_index, to_index,
                                                               last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index),
                                                               reference(from_index, to_index)))
            break

    if all_tests_passed:
        passed()
