from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for r, c in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if r >= n or r < 0 or c >= m or c < 0 or grid[r][c] == 0:
                            res += 1
        return res


def test():
    print(Solution().islandPerimeter(grid=[
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]))

    print(Solution().islandPerimeter(grid=[
        [1, 0]
    ]))


if __name__ == '__main__':
    test()
