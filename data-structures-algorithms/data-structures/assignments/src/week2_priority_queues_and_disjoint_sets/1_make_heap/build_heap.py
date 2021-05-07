# python3


def build_heap_efficient(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def parent(i):
    return (i - 1) // 2


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size, self.swaps = 0, []
        self.data = [0] * max_size

    def sift_up(self, i):
        while i > 0 and self.data[parent(i)] > self.data[i]:
            self.data[parent(i)], self.data[i] = self.data[i], self.data[parent(i)]
            self.swaps.append((parent(i), i))
            i = parent(i)

    def sift_down(self, i):
        min_index = i
        l = left_child(i)
        if l < self.size and self.data[l] < self.data[min_index]:
            min_index = l
        r = right_child(i)
        if r < self.size and self.data[r] < self.data[min_index]:
            min_index = r
        if i != min_index:
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            self.swaps.append((i, min_index))
            self.sift_down(min_index)

    def insert(self, element):
        if self.size == self.max_size:
            raise ValueError
        self.size = self.size + 1
        self.data[self.size - 1] = element
        self.sift_up(self.size - 1)

    def extract_min(self):
        result = self.data[0]
        self.data[0] = self.data[self.size - 1]
        self.size -= 1
        self.sift_down(0)
        return result

    def remove(self, i):
        self.data[i] = 10**18
        self.sift_up(i)
        self.extract_min()

    def change_priority(self, i, element):
        old_parent = self.data[i]
        self.data[i] = element
        if element > old_parent:
            self.sift_up(i)
        else:
            self.sift_down(i)

    def get_min(self):
        return self.data[0]


def build_heap(data):
    n = len(data)
    min_heap = MinHeap(n)

    min_heap.data = data
    min_heap.size = n

    for i in range(n // 2 - 1, -1, -1):
        min_heap.sift_down(i)

    return min_heap.swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
