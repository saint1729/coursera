from test_helper import run_common_tests, failed, passed, check_tests_pass
from money_change import money_change


def reference(money):
    assert 0 <= money <= 10 ** 3
    return (money // 10) + ((money % 10) // 5) + (money % 5)


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("money_change_unit_tests.py")

    all_tests_passed = True
    for m in range(10 ** 3):
        if money_change(m) != reference(m):
            all_tests_passed = False
            failed("Wrong answer for money={}".format(m))
            break

    if all_tests_passed:
        passed()
