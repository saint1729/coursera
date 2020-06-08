import unittest
from maximum_ad_revenue import max_dot_product, max_dot_product_naive


class TestMaxDotProduct(unittest.TestCase):
    def test_small(self):
        for (first_sequence, second_sequence) in [
            ([1], [2]),
            ([2], [1]),
            ([1], [1]),
            ([1, 2], [5, 10]),
            ([2, 1], [5, 10]),
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
            ([17, 12, 20], [19, 2, 3]),
            type here
        ]:
            self.assertEqual(
                max_dot_product(list(first_sequence), list(second_sequence)),
                max_dot_product_naive(first_sequence, second_sequence)
            )

    def test_large(self):
        n = 10 ** 3
        self.assertEqual(max_dot_product([0] * n, [0] * n), 0)
        self.assertEqual(max_dot_product([1] * n, [1] * n), n)
        type here



if __name__ == '__main__':
    unittest.main()
