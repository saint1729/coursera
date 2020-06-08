from test_helper import run_common_tests, failed, passed, check_tests_pass
from maximum_gold import maximum_gold


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("maximum_gold_unit_tests.py")

    all_tests_passed = True

    for capacity, weights, answer in (
            (10, (1, 4, 8), 9),
            (20, (5, 7, 12, 18), 19),
            (10, (3, 5, 3, 3, 5), 10),
            (10, (3, 5, 3, 3, 5), 10),
            (500, (342, 381, 230, 381, 206, 393, 364, 319, 279, 385, 345, 263, 365, 281, 298, 247, 239, 201, 378, 351), 499)
    ):
        if maximum_gold(capacity, weights) != answer:
            all_tests_passed = False
            failed("Wrong answer for capacity={}, weights={}".format(capacity, weights))
            break

    if all_tests_passed:
        passed()
