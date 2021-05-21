# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((next, i))
        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            left = opening_brackets_stack.pop(-1)
            if not are_matching(left[0], next):
                return i + 1
    return "Success" if len(opening_brackets_stack) == 0 else opening_brackets_stack.pop(-1)[1] + 1


def main():
    text = input()
    print(find_mismatch(text))


if __name__ == "__main__":
    main()
