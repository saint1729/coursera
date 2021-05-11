# python3
import random


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


def poly_hash(s, p, x):
    h = 0
    for i in range(len(s) - 1, -1, -1):
        h = (h * x + ord(s[i])) % p
    return h


def pre_compute_hashes(text, len_pat, p, x):
    len_text = len(text)
    h = [0] * (len_text - len_pat + 1)
    s = text[(len_text - len_pat): len_text]
    h[len_text - len_pat] = poly_hash(s, p, x)
    y = 1
    for i in range(len_pat):
        y = (y * x) % p
    for i in range(len_text - len_pat - 1, -1, -1):
        h[i] = (x * h[i + 1] + ord(text[i]) - y * ord(text[i + len_pat])) % p
    return h


def are_equal(text, i, j, pattern):
    len_pat = len(pattern)
    if j - i + 1 != len_pat:
        return False
    for k in range(len_pat):
        if text[k + i] != pattern[k]:
            return False
    return True


def rabin_karp(pattern, text):
    p1 = (10**9 + 7)
    p2 = (10**9 + 9)
    x = random.randint(1, p1 - 1)
    result = []
    p1_hash = poly_hash(pattern, p1, x)
    p2_hash = poly_hash(pattern, p2, x)
    len_txt, len_pat = len(text), len(pattern)
    h1 = pre_compute_hashes(text, len_pat, p1, x)
    h2 = pre_compute_hashes(text, len_pat, p2, x)
    for i in range(len_txt - len_pat + 1):
        if p1_hash != h1[i] or p2_hash != h2[i]:
            continue
        result.append(i)
    return result


if __name__ == '__main__':
    print_occurrences(rabin_karp(*read_input()))
