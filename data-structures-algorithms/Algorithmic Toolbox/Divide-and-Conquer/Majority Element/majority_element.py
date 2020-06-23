# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element_util(elements, low, high):
    if low == high:
        return elements[low]
    else:
        mid = low + (high - low) // 2

        left_majority = majority_element_util(elements, low, mid)
        right_majority = majority_element_util(elements, mid + 1, high)

        if left_majority == right_majority:
            return left_majority

        left_majority_count = elements[low: (high + 1)].count(left_majority)
        right_majority_count = elements[low: (high + 1)].count(right_majority)

        return left_majority if (left_majority_count > right_majority_count) else right_majority


def majority_element(elements):
    assert len(elements) <= 10 ** 5

    result = majority_element_util(elements, 0, len(elements) - 1)

    return 1 if (elements.count(result) > (len(elements) // 2)) else 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
