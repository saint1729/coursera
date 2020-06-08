from test_helper import run_common_tests, failed, passed, check_tests_pass
from lcs3 import lcs3
from random import randint, seed


def ref(a, b, c):
    d = [[[0 for _ in range(len(c) + 1)] for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            for k in range(len(c) + 1):
                if i < len(a):
                    d[i + 1][j][k] = max(d[i][j][k], d[i + 1][j][k])
                if j < len(b):
                    d[i][j + 1][k] = max(d[i][j][k], d[i][j + 1][k])
                if k < len(c):
                    d[i][j][k + 1] = max(d[i][j][k], d[i][j][k + 1])
                if i < len(a) and j < len(b) and k < len(c) and a[i] == b[j] == c[k]:
                    d[i + 1][j + 1][k + 1] = max(d[i + 1][j + 1][k + 1], d[i][j][k] + 1)
    return d[len(a)][len(b)][len(c)]


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("lcs3_unit_tests.py")

    seed(239)

    all_tests_passed = True

    for _ in range(10):
        for n in (3, 5, 20, 10):
            for m in (2, 3, 4, 10, 100):
                lena = randint(1, n)
                lenb = randint(1, n)
                lenc = randint(1, n)
                a = [randint(1, m) for _ in range(lena)]
                b = [randint(1, m) for _ in range(lenb)]
                c = [randint(1, m) for _ in range(lenc)]

                if lcs3(a, b, c) != ref(a, b, c):
                    all_tests_passed = False
                    failed("Wrong answer: {}; {}; {}".format(a, b, c))
                    break

    if all_tests_passed:
        passed()
