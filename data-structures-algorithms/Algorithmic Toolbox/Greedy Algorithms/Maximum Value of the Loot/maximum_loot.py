# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    combined = sorted(zip([float(price) / weight for weight, price in zip(weights, prices)],
                          weights, prices), key=lambda x: -x[0])

    ans = 0

    i, size = 0, len(combined)
    while (capacity > 0) and (i < size):
        ans += (combined[i][2] * min(capacity / combined[i][1], 1.0))
        capacity -= combined[i][1]
        i += 1

    return ans


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
