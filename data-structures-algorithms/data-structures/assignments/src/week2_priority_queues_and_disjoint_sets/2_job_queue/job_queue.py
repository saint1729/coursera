# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs_naive(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


class Node(object):
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f'Node value: {self.val}'

    def __lt__(self, other):
        return self.val[0] < other.val[0] if self.val[0] != other.val[0] else self.val[1] < other.val[1]


def assign_jobs(n_workers, jobs):
    result = []
    heap = []
    heapq.heapify(heap)

    n = len(jobs)
    for i in range(n_workers):
        heapq.heappush(heap, Node([0, i]))

    for i in range(n):
        node = heapq.heappop(heap)
        result.append(AssignedJob(worker=node.val[1], started_at=node.val[0]))
        heapq.heappush(heap, Node([node.val[0] + jobs[i], node.val[1]]))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
