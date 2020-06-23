# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search_util(keys, value, start, end):
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if keys[mid] == value:
        return mid
    elif keys[mid] > value:
        return binary_search_util(keys, value, start, mid - 1)
    else:
        return binary_search_util(keys, value, mid + 1, end)


def binary_search(keys, query):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    # assert 1 <= len(keys) <= 3 * 10 ** 4

    return binary_search_util(keys, query, 0, len(keys) - 1)


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
