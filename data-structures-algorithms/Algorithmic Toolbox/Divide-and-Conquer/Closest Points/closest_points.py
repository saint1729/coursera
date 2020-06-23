# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_split_distance_squared(points, root_delta):
    min_split_dist_sq = root_delta ** 2

    total_split_points = len(points)
    for index, point in enumerate(points):
        j = index + 1
        while (j < total_split_points) and ((points[j].y - point.y) < root_delta):
            min_split_dist_sq = min(min_split_dist_sq, distance_squared(points[j], point))
            j += 1

    return min_split_dist_sq


def minimum_distance_squared_util(points_x, points_yx):
    if len(points_x) < 4:
        return minimum_distance_squared_naive(points_x)

    mid = len(points_x) // 2

    left_points_x = points_x[:mid]
    right_points_x = points_x[mid:]

    mid_point_x = points_x[mid].x

    left_points_yx = []
    right_points_yx = []

    for point in points_yx:
        if point.x < mid_point_x:
            left_points_yx.append(point)
        else:
            right_points_yx.append(point)

    left_min_dist = minimum_distance_squared_util(left_points_x, left_points_yx)
    right_min_dist = minimum_distance_squared_util(right_points_x, right_points_yx)

    delta = min(left_min_dist, right_min_dist)

    if delta == 0.0:
        return delta

    split_points = []

    root_delta = sqrt(delta)

    for point in points_yx:
        if abs(mid_point_x - point.x) < root_delta:
            split_points.append(point)

    min_split_dist_sq = minimum_split_distance_squared(split_points, root_delta)

    return min(delta, min_split_dist_sq)


def minimum_distance_squared(points):
    points_x = sorted(points, key=lambda point: point.x)
    points_yx = sorted(points, key=lambda point: (point.y, point.x))

    return minimum_distance_squared_util(points_x, points_yx)


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
