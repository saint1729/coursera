# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    a = 0
    b = 1
    c = 1
    i = 2

    while i < n:
        a = b
        b = c
        c = a + b
        i += 1

    return c

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
