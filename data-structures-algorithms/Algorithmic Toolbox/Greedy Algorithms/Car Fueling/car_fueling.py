# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    fuel = m

    stops.insert(0, 0)
    stops.append(d)
    minimum_stops, prev, curr, distance_covered, n = -1, 0, 1, 0, len(stops)

    while curr < n:
        while (fuel >= 0) and (curr < n):
            fuel -= (stops[curr] - stops[curr - 1])
            curr += 1
        if (fuel < 0) and (curr == (prev + 1)):
            return -1
        elif fuel < 0:
            curr -= 1
        fuel = m
        prev = curr
        minimum_stops += 1

    return minimum_stops


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
