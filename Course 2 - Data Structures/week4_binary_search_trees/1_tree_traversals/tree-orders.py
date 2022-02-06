# python3
import queue
import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self, size, tree_nodes):
        self.n = int(size)     # self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, tree_nodes[i].split())  # sys.stdin.readline().split())
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

    def test(self, outputs):
        in_order = " ".join([str(x) for x in self.inOrder(0)])
        pre_order = " ".join([str(x) for x in self.preOrder(0)])
        post_order = " ".join([str(x) for x in self.postOrder(0)])
        level_order = " ".join([str(x) for x in self.levelOrder(0)])
        try:
            assert outputs[0] == in_order
            print('in_order test success!')
        except:
            print('in_order test failed!')
            print(f'anticipated: {outputs[0]}')
            print(f'returned: {in_order}')
        try:
            assert outputs[1] == pre_order
            print('pre_order test success!')
        except:
            print('pre_order test failed!')
            print(f'anticipated: {outputs[1]}')
            print(f'returned: {pre_order}')
        try:
            assert outputs[2] == post_order
            print('post_order test success!')
        except:
            print('post_order test failed!')
            print(f'anticipated: {outputs[2]}')
            print(f'returned: {post_order}')
        try:
            assert outputs[3] == level_order
            print('level_order test success!')
        except:
            print('level_order test failed!')
            print(f'anticipated: {outputs[3]}')
            print(f'returned: {level_order}')


def main():
    for i in range(2):
        print(f'test case {i}')
        file_name = r'C:\Users\qz256\PycharmProjects\Coursera-Data-Structures-and-Algorithms-Specialization' \
                    r'\Course 2 - Data Structures\week4_binary_search_trees\1_tree_traversals\tests\test' + str(i)
        file = open(file_name, 'r')
        lines = file.read().splitlines()
        size, tree_nodes, outputs = lines[0], lines[1:-4], lines[-4:]
        tree = TreeOrders()
        tree.read(size, tree_nodes)
        tree.test(outputs)


threading.Thread(target=main).start()
