from test_helper import run_common_tests, failed, passed, check_tests_pass
from majority_element import majority_element


def reference(elements):
    table = {}
    for e in elements:
        if e in table:
            table[e] += 1
        else:
            table[e] = 1

    for e in table:
        if table[e] > len(elements) / 2:
            return 1

    return 0


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("majority_element_unit_tests.py")

    all_tests_passed = True
    for elements, answer in [
        ([1, 1, 2], 1),
        ([1, 2], 0),
        ([7, 8, 7], 1),
    ]:
        if majority_element(elements) != answer:
            all_tests_passed = False
            failed("Wrong answer for elements={}".format(elements))
            break

    if all_tests_passed:
        passed()
