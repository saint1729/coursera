# python3

from itertools import permutations
import functools


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def compare_numbers(a, b):
    ab = a + b
    ba = b + a
    return int(ba) - int(ab)


def largest_number(numbers):
    numbers = map(str, numbers)
    numbers = sorted(numbers, key=functools.cmp_to_key(compare_numbers))
    return int("".join(numbers))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
