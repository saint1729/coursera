from test_helper import run_common_tests, failed, passed, check_tests_pass
from arithmetic_expression import find_maximum_value


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("arithmetic_expression_unit_tests.py")

    all_tests_passed = True

    for s, answer in (
        ("5", 5),
        ("2+3", 5),
        ("2-3", -1),
        ("5-8+7*4-8+9", 200),
        ("2-3", -1),
        ("9*9*9*9", 9 * 9 * 9 * 9),
        ("1-1", 0),
        ("7", 7),
        ("1+2+3+4+5+6+7+8+9", 45),
    ):
        if find_maximum_value(s) != answer:
            all_tests_passed = False
            failed("Wrong answer for {}".format(s))
            break

    if all_tests_passed:
        passed()
