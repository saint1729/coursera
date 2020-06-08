from test_helper import run_common_tests, failed, passed, check_tests_pass
from car_fueling import compute_min_number_of_refills


def reference(distance, tank, stops):
    stops = [0] + stops + [distance]
    num_refills, cur_refill = 0, 0
    while cur_refill <= len(stops) - 2:
        last_refill = cur_refill
        while cur_refill <= len(stops) - 2 and stops[cur_refill + 1] - stops[last_refill] <= tank:
            cur_refill += 1
        if cur_refill == last_refill:
            return -1
        if cur_refill <= len(stops) - 2:
            num_refills += 1

    return num_refills


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("car_fueling_unit_tests.py")

    all_tests_passed = True
    for (d, m, stops) in [(500, 200, [100, 200, 300, 400])]:
        if reference(d, m, stops) != compute_min_number_of_refills(d, m, stops):
            all_tests_passed = False
            failed("Wrong answer for d={}, m={}, stops={}".format(d, m, stops))
            break

    if all_tests_passed:
        passed()
