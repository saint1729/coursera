from test_helper import run_common_tests, failed, passed, check_tests_pass
from money_change_again import change, change_naive
from random import randint


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("money_change_again_unit_tests.py")

    all_tests_passed = True

    for _ in range(20):
        money = randint(1, 100)
        if change_naive(money) != change(money):
            all_tests_passed = False
            failed("Wrong answer for money={}".format(money))
            break

    if all_tests_passed:
        passed()
