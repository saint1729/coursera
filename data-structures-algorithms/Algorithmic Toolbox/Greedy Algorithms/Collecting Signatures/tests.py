from test_helper import run_common_tests, failed, passed, check_tests_pass
from collecting_signatures import compute_optimal_points, Segment


def reference(segments):
    points = []
    segments = sorted(segments, key=lambda x: x.end)
    limit = -1
    for segment in segments:
        if limit < segment.start:
            limit = segment.end
            points.append(segment.end)
    return points


if __name__ == '__main__':
    run_common_tests()
    check_tests_pass("collecting_signatures_unit_tests.py")

    all_tests_passed = True
    for segments in [
        [Segment(48, 90), Segment(1, 60), Segment(49, 51), Segment(18, 80)]
    ]:
        if reference(segments) != compute_optimal_points(segments):
            all_tests_passed = False
            failed("Wrong answer for segments: {}".format(segments))
            break

    if all_tests_passed:
        passed()
