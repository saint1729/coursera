# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def get_pisano_period(m):
    previous = 0
    current = 1

    period = 1

    while True:
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            break
        period += 1

    return period


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    period = get_pisano_period(m)
    n %= period

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    # print(get_pisano_period(input_m))
    print(fibonacci_number_again(input_n, input_m))
