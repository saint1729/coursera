# python3
import random
import sys


def get_hash(h, a, l, x, p):
    return (h[a + l] - pow(x, l, p) * h[a]) % p


class Solver:
    def __init__(self, s):
        self.s = s
        self.p1, self.p2 = (10**9) + 7, (10**9) + 9
        self.x = random.randint(1, self.p1)
        self.h1, self.h2 = pre_compute_hashes(s, self.p1, self.p2, self.x)

    def ask(self, a, b, l):
        out1 = (get_hash(self.h1, a, l, self.x, self.p1) == get_hash(self.h1, b, l, self.x, self.p1))
        out2 = (get_hash(self.h2, a, l, self.x, self.p2) == get_hash(self.h2, b, l, self.x, self.p2))
        return out1 and out2


def pre_compute_hashes(text, p1, p2, x):
    len_text = len(text) + 1
    h1, h2 = [0] * len_text, [0] * len_text
    for i in range(1, len_text):
        h1[i] = (x * h1[i - 1] + ord(text[i - 1])) % p1
        h2[i] = (x * h2[i - 1] + ord(text[i - 1])) % p2
    return h1, h2


if __name__ == '__main__':
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    solver = Solver(s)
    for i in range(q):
        a, b, l = map(int, sys.stdin.readline().split())
        if solver.ask(a, b, l):
            print("Yes")
        else:
            print("No")
