# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def merge_elements(array, start, end, mid):
    i, j = start, mid + 1
    buffer = [0] * (end - start + 1)
    index, count = 0, 0
    while (i <= mid) and (j <= end):
        if array[i] <= array[j]:
            buffer[index] = array[i]
            i += 1
        else:
            buffer[index] = array[j]
            count += (mid - i + 1)
            j += 1
        index += 1

    while i <= mid:
        buffer[index] = array[i]
        index += 1
        i += 1

    while j <= end:
        buffer[index] = array[j]
        index += 1
        j += 1

    for i in range(start, end + 1):
        array[i] = buffer[i - start]

    return count


def compute_inversions_util(array, start, end):
    if start >= end:
        return 0
    mid = start + (end - start) // 2
    inversions = compute_inversions_util(array, start, mid)
    inversions += compute_inversions_util(array, mid + 1, end)
    inversions += merge_elements(array, start, end, mid)
    return inversions


def compute_inversions(array):
    array2 = array[:]
    return compute_inversions_util(array2, 0, len(array2) - 1)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
