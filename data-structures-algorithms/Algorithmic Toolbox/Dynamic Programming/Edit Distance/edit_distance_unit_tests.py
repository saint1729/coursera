import unittest
from edit_distance import edit_distance


class EditDistance(unittest.TestCase):
    def test(self):
        for first_string, second_string, answer in (
            ("ab", "ab", 0),
            ("short", "ports", 3),
            ("editing", "distance", 5),
            ("a" * 100, "a" * 100, 0),
            ("ab" * 50, "ba" * 50, 2),
            type here
        ):
            self.assertEqual(edit_distance(first_string, second_string), answer)


if __name__ == '__main__':
    unittest.main()
