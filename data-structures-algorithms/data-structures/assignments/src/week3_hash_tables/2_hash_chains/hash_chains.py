# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


def write_search_result(was_found):
    print('yes' if was_found else 'no')


def write_chain(chain):
    print(' '.join(chain))


def read_query():
    return Query(input().split())


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for i in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            write_chain([cur for cur in reversed(self.elems[query.ind])])
        else:
            bucket_index = -1
            try:
                bucket_index = self._hash_func(query.s)
                actual_index = self.elems[bucket_index].index(query.s)
            except ValueError:
                actual_index = -1
            if query.type == 'find':
                write_search_result(actual_index != -1)
            elif query.type == 'add':
                if actual_index == -1:
                    self.elems[bucket_index].append(query.s)
            else:
                if actual_index != -1:
                    self.elems[bucket_index].remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
