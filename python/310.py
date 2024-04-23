from collections import defaultdict
from typing import List
from queue import SimpleQueue


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        nodes = defaultdict(list)
        degrees = [0] * n
        for u, w in edges:
            nodes[u].append(w)
            nodes[w].append(u)
            degrees[u] += 1
            degrees[w] += 1

        q = SimpleQueue()
        for w in nodes:
            if degrees[w] == 1:
                q.put(w)

        remain = n
        while remain > 2:
            size = q.qsize()
            remain -= size
            for _ in range(size):
                leaf = q.get()
                for w in nodes[leaf]:
                    degrees[w] -= 1
                    if degrees[w] == 1:
                        q.put(w)
        res = []
        while not q.empty():
            e = q.get()
            res.append(e)

        return res


def test():
    print(Solution().findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
    print(Solution().findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
    print(Solution().findMinHeightTrees(n=3, edges=[[0, 1], [0, 2]]))


if __name__ == '__main__':
    test()
