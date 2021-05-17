#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    tree.append([None, -1, -1])

    stack = []

    root = tree[0]
    prev = -(2 ** 31)
    while True:
        if root[0] is not None:
            stack.append(root)
            root = tree[root[1]]
        else:
            if len(stack) == 0:
                break
            root = stack.pop(-1)
            if (root[0] < prev) or (root[0] == tree[root[1]][0]):
                tree.pop(-1)
                return False
            prev = root[0]
            root = tree[root[2]]

    tree.pop(-1)
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


if __name__ == "__main__":
    threading.Thread(target=main).start()
