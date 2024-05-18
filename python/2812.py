from typing import List
from queue import SimpleQueue


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]

        def bfs_manhattan(q, d):
            while q.qsize() > 0:
                wx, wy = q.get()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    sx, sy = wx + dx, wy + dy
                    if 0 <= sx < n and 0 <= sy < n and (sx, sy) not in d:
                        q.put((sx, sy))
                        d[(sx, sy)] = d[(wx, wy)] + 1
                        dp[sx][sy] = d[(sx, sy)]

        def bfs(val):
            if dp[0][0] < val or dp[n - 1][n - 1] < val:
                return False
            q = SimpleQueue()
            q.put((0, 0))
            q.put((n - 1, n - 1))
            visited = {(0, 0): 0, (n - 1, n - 1): 1}
            while q.qsize() > 0:
                wx, wy = q.get()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    sx, sy = wx + dx, wy + dy
                    if 0 <= sx < n and 0 <= sy < n and dp[sx][sy] >= val:
                        if (sx, sy) not in visited:
                            q.put((sx, sy))
                            visited[(sx, sy)] = visited[(wx, wy)]
                        elif visited[(sx, sy)] != visited[(wx, wy)]:
                            return True
            return False

        queue = SimpleQueue()
        distances = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.put((i, j))
                    distances[(i, j)] = 0

        bfs_manhattan(queue, distances)

        res = 0
        lo, hi = 1, n - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if bfs(mi):
                res = max(res, mi)
                lo = mi + 1
            else:
                hi = mi - 1

        return res


def test():
    print("test1")
    Solution().maximumSafenessFactor(grid=[
        [0, 1],
        [1, 0]
    ])
    print("test2")
    Solution().maximumSafenessFactor(grid=[
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0]
    ])
    print("test3")
    Solution().maximumSafenessFactor(grid=[[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                                           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                                           [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                           [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
                                           [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                           [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                                           [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                                           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                                           [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0]]
                                     )


if __name__ == '__main__':
    test()
