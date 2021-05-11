# python3
import random
import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')


def solve_naive(s, t):
    ans = Answer(0, 0, 0)
    for i in range(len(s)):
        for j in range(len(t)):
            for l in range(min(len(s) - i, len(t) - j) + 1):
                if (l > ans.len) and (s[i:i + l] == t[j:j + l]):
                    ans = Answer(i, j, l)
    return ans


def get_hash(h, a, l, x, p):
    return (h[a + l] - pow(x, l, p) * h[a]) % p


def pre_compute_hashes(s, p1, p2, x):
    len_s = len(s)
    h1, h2 = [0] * (len_s + 1), [0] * (len_s + 1)
    for i in range(len_s):
        h1[i + 1] = (x * h1[i] + ord(s[i])) % p1
        h2[i + 1] = (x * h2[i] + ord(s[i])) % p2
    return h1, h2


def found_common(small, big, curr_len):
    len_small = len(small)
    len_big = len(big)
    p1, p2 = (10**9) + 7, (10**9) + 9
    x = random.randint(1, p1)
    h1_small, h2_small = pre_compute_hashes(small, p1, p2, x)
    h1_big, h2_big = pre_compute_hashes(big, p1, p2, x)
    h1_small_table, h2_small_table = {}, {}
    for i in range(len_small - curr_len + 1):
        h1_small_table[get_hash(h1_small, i, curr_len, x, p1)] = i
        h2_small_table[get_hash(h2_small, i, curr_len, x, p2)] = i
    for i in range(len_big - curr_len + 1):
        h1_big_val = get_hash(h1_big, i, curr_len, x, p1)
        h2_big_val = get_hash(h2_big, i, curr_len, x, p2)
        if h1_big_val in h1_small_table and h2_big_val in h2_small_table:
            if h1_small_table[h1_big_val] == h2_small_table[h2_big_val]:
                return {"present": True, "small": h1_small_table[h1_big_val], "big": i}
    return {"present": False}


def solve_util(small, big):
    ans = Answer(0, 0, 0)
    len_small = len(small)
    low, high = 1, len_small
    while low <= high:
        curr = low + (high - low) // 2
        result = found_common(small, big, curr)
        if not result["present"]:
            high = curr - 1
        else:
            ans = Answer(result["small"], result["big"], curr)
            low = curr + 1
    return ans


def solve(s, t):
    len_s = len(s)
    len_t = len(t)
    if len_s > len_t:
        ans = solve_util(t, s)
        ans = Answer(ans.j, ans.i, ans.len)
    else:
        ans = solve_util(s, t)
    return ans


if __name__ == "__main__":
    for line in sys.stdin.readlines():
        s, t = line.split()
        ans = solve(s, t)
        print(ans.i, ans.j, ans.len)
