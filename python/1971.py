from typing import List
from queue import SimpleQueue


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        nodes = [[] for _ in range(n)]
        for u, v in edges:
            nodes[u].append(v)
            nodes[v].append(u)

        q = SimpleQueue()
        q.put(source)
        visited = {source}

        while not q.empty():
            u = q.get()
            for w in nodes[u]:
                if w not in visited:
                    if w == destination:
                        return True
                    q.put(w)
                    visited.add(w)
        return False


def test():
    print(Solution().validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5))
    print(Solution().validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))
    print(Solution().validPath(n=10,
                               edges=[[0, 7], [0, 8], [6, 1], [2, 0], [0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]],
                               source=7, destination=5))


if __name__ == '__main__':
    test()
