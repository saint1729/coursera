from test_helper import run_common_tests, failed, passed, check_tests_pass
from maximum_salary import largest_number


def reference(numbers):
    numbers = list(map(str, numbers))

    for _ in numbers:
        for i in range(len(numbers) - 1):
            if numbers[i] + numbers[i + 1] < numbers[i + 1] + numbers[i]:
                t = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = t

    return int("".join(numbers))


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("maximum_salary_unit_tests.py")

    all_tests_passed = True
    for numbers in [
        [2, 21, 23, 211, 213, 231, 232],
        [56, 5, 6, 556, 566, 666, 665, 656]
    ]:
        if reference(numbers) != largest_number(numbers):
            all_tests_passed = False
            failed("Wrong answer for n={}".format(numbers))
            break

    if all_tests_passed:
        passed()
