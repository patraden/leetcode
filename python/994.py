from typing import List
import queue


class Solution:
    adjacency = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = queue.SimpleQueue()
        distance = {}
        empty = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.put((i, j))
                    distance[(i, j)] = 0
                if grid[i][j] == 0:
                    empty += 1

        if empty == n * m:
            return 0

        if q.empty():
            return -1

        res = 0
        while not q.empty():
            wx, wy = q.get()
            for dx, dy in self.adjacency:
                sx, sy = wx + dx, wy + dy
                if 0 <= sx < n and 0 <= sy < m and grid[sx][sy] == 1 and (sx, sy) not in distance:
                    q.put((sx, sy))
                    distance[(sx, sy)] = distance[(wx, wy)] + 1
                    res = max(res, distance[(sx, sy)])

        if len(distance) + empty < n * m:
            return -1
        return res


def test():
    print(Solution().orangesRotting(grid=[
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]))

    print(Solution().orangesRotting(grid=[
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ]))

    print(Solution().orangesRotting(grid=[
        [2, 1]
    ]))

    print(Solution().orangesRotting(grid=[
        [0, 0]
    ]))


if __name__ == '__main__':
    test()
