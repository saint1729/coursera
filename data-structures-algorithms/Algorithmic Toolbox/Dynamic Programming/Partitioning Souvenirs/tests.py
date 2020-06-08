from test_helper import run_common_tests, failed, passed, check_tests_pass
from partition_souvenirs import partition3


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("partition_souvenirs_unit_tests.py")

    all_tests_passed = True

    for values, answer in (
        ((20, ), 0),
        ((7, 7, 7), 1),
        ((3, 3, 3), 1),
        ((3, 3, 3, 3), 0),
        ((1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25), 1),
        ([1]*10, 0),
        ([1]*12, 1),
        ([30] * 20, 0),
        ([30] * 18, 1),
    ):
        if partition3(values) != answer:
            all_tests_passed = False
            failed("Wrong answer for values={}".format(values))
            break

    if all_tests_passed:
        passed()
