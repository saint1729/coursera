from test_helper import run_common_tests, failed, passed, check_tests_pass
from binary_search import binary_search
from random import randrange


def reference(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 10 ** 4

    left, right = 0, len(keys)
    while left + 1 < right:
        ave = (left + right) // 2
        if keys[ave] <= query:
            left = ave
        else:
            right = ave
    if keys[left] != query:
        return -1
    else:
        return left


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("binary_search_unit_tests.py")

    all_tests_passed = True
    for _ in range(20):
        keys = set()
        for i in range(100):
            x = randrange(239239) + 1
            while x in keys:
                x = randrange(239239) + 1
            keys.add(x)
        keys = sorted(list(keys))

        for key in keys:
            for query in (key, key + 1):
                if binary_search(keys, query) != reference(keys, query):
                    all_tests_passed = False
                    failed("Wrong answer for keys={}, query={}".format(keys, query))
                    break

    if all_tests_passed:
        passed()
