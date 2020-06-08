from test_helper import run_common_tests, failed, passed, check_tests_pass
from edit_distance import edit_distance


def reference(s, t):
    sn = len(s)
    tn = len(t)

    f = [[10**9] * (tn + 2) for _ in range(sn + 2)]
    f[0][0] = 0

    def relax(p, q, x):
        f[p][q] = min(f[p][q], x)

    for i in range(sn + 1):
        for j in range(tn + 1):
            if i < sn and j < tn:
                relax(i + 1, j + 1, f[i][j] + (1 if s[i] != t[j] else 0))
            relax(i + 1, j, f[i][j] + 1)
            relax(i, j + 1, f[i][j] + 1)
    return f[sn][tn]


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("edit_distance_unit_tests.py")

    all_tests_passed = True

    for first, second in (
        ("abacabadabacabaeabacab", "aeabacabad"),

    ):
        if edit_distance(first, second) != reference(first, second):
            all_tests_passed = False
            failed("Wrong answer for {} and {}".format(first, second))
            break

    if all_tests_passed:
        passed()
