# python3
import random
import sys


class MisMatchCount:
    count = 0


def get_powers(x, len_pat, p):
    pows = [0] * (len_pat + 1)
    for i in range(len_pat + 1):
        pows[i] = pow(x, i, p)
    return pows


def get_hash(h, a, l, p, pows):
    return (h[a + l] - pows[l] * h[a]) % p


def pre_compute_hashes(s, p1, p2, x):
    len_s = len(s)
    h1 = [0] * (len_s + 1)
    h2 = [0] * (len_s + 1)
    for i in range(len_s):
        h1[i + 1], h2[i + 1] = (x * h1[i] + (ord(s[i]) - ord('a'))) % p1, (x * h2[i] + (ord(s[i]) - ord('a'))) % p2
    return h1, h2


def are_equal(h1, h2, p1, p2, a, b, l, pows):
    return get_hash(h1, a, l, p1, pows) == get_hash(h2, b, l, p2, pows)


def bin_search_recursive(text, pattern, h1_text, h2_text, h1_pat, h2_pat, p1, p2, i, pows, k, low, high,
                         mis_match_count):
    if (low > high) or (mis_match_count.count > k):
        return
    # out1 = are_equal(h1_text, h1_pat, p1, p1, low + i, low, high - low + 1, pows)
    out2 = are_equal(h2_text, h2_pat, p2, p2, low + i, low, high - low + 1, pows)
    if not out2:
        mid = low + (high - low) // 2
        if text[mid + i] != pattern[mid]:
            mis_match_count.count += 1
        bin_search_recursive(text, pattern, h1_text, h2_text, h1_pat, h2_pat, p1, p2, i, pows, k, low, mid - 1,
                             mis_match_count)
        bin_search_recursive(text, pattern, h1_text, h2_text, h1_pat, h2_pat, p1, p2, i, pows, k, mid + 1, high,
                             mis_match_count)


def solve(k, text, pattern, p1, p2, x, pows):
    h1_text, h2_text = pre_compute_hashes(text, p1, p2, x)
    h1_pat, h2_pat = pre_compute_hashes(pattern, p2, p2, x)
    len_text = len(text)
    len_pat = len(pattern)
    ans = []
    for i in range(len_text - len_pat + 1):
        low, high = 0, len_pat - 1
        mis_match_count = MisMatchCount()
        bin_search_recursive(text, pattern, h1_text, h2_text, h1_pat, h2_pat, p1, p2, i, pows, k, low, high,
                             mis_match_count)
        if mis_match_count.count <= k:
            ans.append(i)

    return ans


if __name__ == '__main__':
    z = 10 ** 9
    p1, p2 = z + 7, z + 9
    x = random.randint(1, p1 - 1)
    max_pat_len = 100000
    pows = get_powers(x, max_pat_len, p2)
    for line in sys.stdin.readlines():
        k, t, p = line.split()
        ans = solve(int(k), t, p, p1, p2, x, pows)
        print(len(ans), *ans)
