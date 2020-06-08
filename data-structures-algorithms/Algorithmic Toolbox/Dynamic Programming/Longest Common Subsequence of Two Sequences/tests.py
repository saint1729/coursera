from test_helper import run_common_tests, failed, passed, check_tests_pass
from lcs2 import lcs2


def reference(a, b):
    n, m = len(a), len(b)
    t = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                t[i][j] = max(t[i - 1][j - 1] + 1, t[i][j - 1], t[i - 1][j])
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])

    return t[n][m]


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("lcs2_unit_tests.py")

    all_tests_passed = True

    for first, second in (
        ([1, 2] * 50, [2, 1] * 50),
        ([0] * 10, [i % 3 for i in range(10)]),
    ):
        if lcs2(first, second) != reference(first, second):
            all_tests_passed = False
            failed("Wrong answer for {} and {}".format(first, second))
            break

    if all_tests_passed:
        passed()
