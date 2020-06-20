# python3
import math

def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    maximum_prizes_minus_one = math.floor((-1 + (1 + 8 * n) ** 0.5) / 2) - 1

    index = 0
    while index < maximum_prizes_minus_one:
        index += 1
        summands.append(index)

    summands.append(n - (index * (index + 1)) // 2)

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
