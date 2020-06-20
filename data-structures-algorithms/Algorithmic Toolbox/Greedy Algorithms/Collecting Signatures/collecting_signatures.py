# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments.sort(key=lambda x: x.end)
    segments.sort(key=lambda x: x.start)

    optimal_points, index, total_points = [segments[0].end], 1, len(segments)

    while index < total_points:
        if (segments[index].end < segments[index - 1].end) \
                and (optimal_points[-1] > segments[index].end):
            optimal_points[-1] = segments[index].end
        elif (segments[index].start > segments[index - 1].end) \
                or (segments[index].start > optimal_points[-1]):
            optimal_points.append(segments[index].end)
        index += 1

    return optimal_points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
