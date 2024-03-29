from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
                elif i > 0 and j == 0:
                    grid[i][j] += grid[i - 1][j]
                elif j > 0 and i == 0:
                    grid[i][j] += grid[i][j - 1]

        return grid[n - 1][m - 1]


def test():
    print(Solution().minPathSum(
        grid=[
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]))

    print(Solution().minPathSum(
        grid=[
            [1, 2, 3],
            [4, 5, 6],
        ]))

    print(Solution().minPathSum(
        grid=[
            [1, 2, 3],
        ]))

    print(Solution().minPathSum(
        grid=[
            [1],
            [3],
        ]))


if __name__ == '__main__':
    test()
