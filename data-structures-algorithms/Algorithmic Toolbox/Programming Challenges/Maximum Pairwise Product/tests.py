from test_helper import run_common_tests, failed, passed, check_tests_pass
from maximum_pairwise_product import max_pairwise_product

if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("maximum_pairwise_product_unit_tests.py")

    all_tests_passed = True
    tests = [
        ([1, 2], 2),
        ([2, 1], 2),
        ([3, 5], 15),
        ([5, 3], 15),
        ([7, 7], 49),
        ([5, 1, 5], 25),
        ([1, 5, 5], 25),
        ([i + 1 for i in range(10**5)], (10**5 - 1) * (10 ** 5)),
    ]

    for array, answer in tests:
        if max_pairwise_product(array) != answer:
            all_tests_passed = False
            failed("Wrong answer for A={}".format(array))
            break

    if all_tests_passed:
        passed()
