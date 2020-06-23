# python3

from random import randint
# import numpy as np

def partition3(array, left, right):
    pivot = array[left]

    low = left
    mid = left
    high = right

    while mid <= high:
        if array[mid] == pivot:
            mid += 1
        elif array[mid] < pivot:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        elif array[mid] > pivot:
            array[mid], array[high] = array[high], array[mid]
            high -= 1

    return low, mid - 1


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    start_index, end_index = partition3(array, left, right)
    if left < start_index:
        randomized_quick_sort(array, left, start_index - 1)
    if right > end_index:
        randomized_quick_sort(array, end_index + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
    # np.random.seed(100000)  # option for reproducibility
    # elements = np.random.randint(low=1, high=5, size=1).tolist()
    # print(elements)
    # print(len(elements))
    # print(partition3(elements, 0, len(elements) - 1))
    # print(elements)
