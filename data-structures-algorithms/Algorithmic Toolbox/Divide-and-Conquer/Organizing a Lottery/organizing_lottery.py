# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    left = list(zip(starts, [0] * len(starts)))
    mid = list(zip(points, [1] * len(points)))
    right = list(zip(ends, [2] * len(ends)))

    count = [0] * len(points)

    dots = left + mid + right

    dots = sorted(dots, key=lambda x: x[1])
    dots = sorted(dots, key=lambda x: x[0])

    intervals = 0
    counts = dict(zip(points, [0] * len(points)))
    for dot in dots:
        if dot[1] == 0:
            intervals += 1
        elif dot[1] == 2:
            intervals -= 1
        else:
            counts[dot[0]] = intervals

    for index, point in enumerate(points):
        count[index] = counts[point]


    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
