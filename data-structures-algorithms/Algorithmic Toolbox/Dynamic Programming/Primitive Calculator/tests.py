from test_helper import run_common_tests, failed, passed, check_tests_pass
from primitive_calculator import compute_operations


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("primitive_calculator_unit_tests.py")

    all_tests_passed = True

    for n, answer in ((20, 4), (200, 8), (239, 10), (69006, 19)):
        sequence = compute_operations(n)
        if len(sequence) - 1 != answer:
            all_tests_passed = False
            failed("Wrong answer for n={}".format(n))
            break

    if all_tests_passed:
        passed()
