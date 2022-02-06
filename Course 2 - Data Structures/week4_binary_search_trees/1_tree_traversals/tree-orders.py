# python3
import queue
import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self, file_name):
        file = open(file_name, 'r')
        lines = file.read().splitlines()
        # self.n = int(sys.stdin.readline())
        self.n = int(lines[0])
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, lines[i+1].split())  # sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    # DFS: root is the tree's root row index, starts from 0
    def inOrder(self, root):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if root == -1:
            return self.result
        self.result += self.inOrder(self.left[root])
        self.result += [self.key[root]]
        self.result += self.inOrder(self.right[root])
        return self.result

    def preOrder(self, root):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if root == -1:
            return self.result
        self.result += [self.key[root]]
        self.result += self.preOrder(self.left[root])
        self.result += self.preOrder(self.right[root])
        return self.result

    def postOrder(self, root):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if root == -1:
            return self.result
        self.result += self.postOrder(self.left[root])
        self.result += self.postOrder(self.right[root])
        self.result += [self.key[root]]
        return self.result

    # BFS
    def levelOrder(self, root):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if root == -1:
            return self.result
        q = queue.Queue(self.n)
        q.put(root)
        while not q.empty():
            root = q.get()
            self.result += [self.key[root]]
            if self.left[root] != -1:
                q.put(self.left[root])
            if self.right[root] != -1:
                q.put(self.right[root])
        return self.result


def main():
    tree = TreeOrders()
    tree.read(file_name=r'week4_binary_search_trees/1_tree_traversals/tests/test2')
    print(" ".join(str(x) for x in tree.inOrder(0)))
    print(" ".join(str(x) for x in tree.preOrder(0)))
    print(" ".join(str(x) for x in tree.postOrder(0)))
    print(" ".join(str(x) for x in tree.levelOrder(0)))


threading.Thread(target=main).start()
