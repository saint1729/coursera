# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        self.result = []
        self.n = int(sys.stdin.readline())
        self.right = [0 for _ in range(self.n)]
        self.left = [0 for _ in range(self.n)]
        self.key = [0 for _ in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []

        stack = []
        root = (self.key[0], self.left[0], self.right[0])

        self.key.append(-1)
        self.left.append(-1)
        self.right.append(-1)

        while True:
            if root[0] != -1:
                stack.append(root)
                root = (self.key[root[1]], self.left[root[1]], self.right[root[1]])
            else:
                if len(stack) == 0:
                    break
                root = stack.pop(-1)
                self.result.append(root[0])
                root = (self.key[root[2]], self.left[root[2]], self.right[root[2]])

        self.key.pop(-1)
        self.left.pop(-1)
        self.right.pop(-1)

        return self.result

    def preOrder(self):
        self.result = []

        root = (self.key[0], self.left[0], self.right[0])
        stack = [root]
        while not len(stack) == 0:
            root = stack.pop(-1)
            self.result.append(root[0])
            right_index = root[2]
            left_index = root[1]
            if right_index != -1:
                stack.append((self.key[right_index], self.left[right_index], self.right[right_index]))
            if left_index != -1:
                stack.append((self.key[left_index], self.left[left_index], self.right[left_index]))

        return self.result

    def postOrder(self):
        self.result = []

        root = (self.key[0], self.left[0], self.right[0])
        stack1, stack2 = [root], []

        while not len(stack1) == 0:
            root = stack1.pop(-1)
            stack2.append(root)
            left_index = root[1]
            right_index = root[2]
            if left_index != -1:
                stack1.append((self.key[left_index], self.left[left_index], self.right[left_index]))
            if right_index != -1:
                stack1.append((self.key[right_index], self.left[right_index], self.right[right_index]))

        while not len(stack2) == 0:
            self.result.append(stack2.pop(-1)[0])

        return self.result


def main():
    tree = TreeOrders()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


if __name__ == '__main__':
    threading.Thread(target=main).start()
