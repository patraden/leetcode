from typing import List


class UnionFind:
    def __init__(self, qty):
        self.parent = [i for i in range(qty)]
        self.size = [1] * qty
        self.count = qty

    # Time: O(logn) | Space: O(1)
    def find(self, node):
        while node != self.parent[node]:
            # path compression
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    # Time: O(1) | Space: O(1)
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        # already in the same set
        if root1 == root2:
            return

        if self.size[root1] > self.size[root2]:
            self.parent[root2] = root1
            self.size[root1] += 1
        else:
            self.parent[root1] = root2
            self.size[root2] += 1

        self.count -= 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        remains1 = []
        remains2 = []
        res = 0

        for t, u, v in edges:
            if t == 3:
                if uf.find(u - 1) != uf.find(v - 1):
                    uf.union(u - 1, v - 1)
                    res += 1
            elif t == 1:
                remains1.append((t, u, v))
            elif t == 2:
                remains2.append((t, u, v))

        uf2 = UnionFind(n)
        uf2.parent = uf.parent.copy()
        uf2.size = uf.size.copy()
        uf2.count = uf.count

        for t, u, v in remains1:
            if uf.find(u - 1) != uf.find(v - 1):
                uf.union(u - 1, v - 1)
                res += 1

        # print(uf.parent, uf.size, uf.count)
        if uf.count > 1:
            return -1

        for t, u, v in remains2:
            if uf2.find(u - 1) != uf2.find(v - 1):
                uf2.union(u - 1, v - 1)
                res += 1

        # print(uf2.parent, uf2.size, uf2.count)
        if uf2.count > 1:
            return -1

        return len(edges) - res


def test():
    print(Solution().maxNumEdgesToRemove(n=4, edges=[
        [3, 1, 2], [3, 2, 3], [1, 1, 3],
        [1, 2, 4], [1, 1, 2], [2, 3, 4]
    ]))
    print(Solution().maxNumEdgesToRemove(n=4, edges=[
        [3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]
    ]))
    print(Solution().maxNumEdgesToRemove(n=4, edges=[
        [3, 2, 3], [1, 1, 2], [2, 3, 4]
    ]))


if __name__ == '__main__':
    test()
