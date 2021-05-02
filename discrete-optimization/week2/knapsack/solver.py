#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(item_count):
        line = lines[i + 1]
        parts = line.split()
        # if (int(parts[1]) <= capacity) and (int(parts[1]) > 0):
        items.append(Item(i, int(parts[0]), int(parts[1])))

    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    n = len(items)
    value = 0
    exact = 0
    taken = [0] * n

    # value = rec_o(capacity, n - 1, items)

    # value, taken = dp_o(capacity, n, items)

    # dp = [-1 for _ in range(capacity + 1)]
    # dp_mem_o(capacity, items, dp, taken)

    # value = dp[-1]

    max_estimate = lin_relax_bound(capacity, items)
    value = max_estimate

    print_power_set([1, 2, 3], 0, 0)

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


def rec_o(k, j, items):
    if j == 0:
        return 0
    elif items[j].weight <= k:
        return max(rec_o(k, j - 1, items), items[j].value + rec_o(k - items[j].weight, j - 1, items))
    else:
        return rec_o(k, j - 1, items)


def dp_o(K, n, items):
    taken = [0] * n

    dp = [[0 for _ in range(n + 1)] for _ in range(K + 1)]

    for i in range(1, n + 1):
        for j in range(1, K + 1):
            if items[i - 1].weight <= j:
                dp[j][i] = max(dp[j][i - 1], items[i - 1].value + dp[j - items[i - 1].weight][i - 1])
            else:
                dp[j][i] = dp[j][i - 1]

    i, j = n, K
    while (i > 0) and (j > 0):
        if dp[j][i] != dp[j][i - 1]:
            taken[i - 1] = 1
            j -= items[i - 1].weight
        i -= 1

    return dp[K][n], taken


def branch_and_bound(value, room, estimate):
    pass


def print_power_set(l, start, current):
    if start == len(l):
        return

    print(l[start:current])

    for i in range(current + 1, len(l)):
        current += 1
        print_power_set(l, current, i)
        current -= 1


def lin_relax_bound(K, items):
    n = len(items)

    total_val, i = 0, 0

    while K > 0 and i < n:
        K -= items[i].weight
        total_val = total_val + items[i].value
        i += 1

    if K < 0:
        total_val += (items[i - 1].value * (K / items[i - 1].weight))

    return total_val


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py '
            './data/ks_4_0)')
