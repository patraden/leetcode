from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        n, m = len(grid), len(grid[0])

        if grid[0][0] == 1:
            return 0

        grid[0][0] = 1

        for i in range(n):
            for j in range(m):
                if not (i == 0 and j ==0) and grid[i][j] == 1:
                    grid[i][j] = 0
                elif i > 0 and j > 0:
                    grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
                elif i > 0 and j == 0:
                    grid[i][j] = grid[i - 1][j]
                elif j > 0 and i == 0:
                    grid[i][j] = grid[i][j - 1]

        return grid[n - 1][m - 1]


def test():
    print(Solution().uniquePathsWithObstacles(
        obstacleGrid=[
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]))

    print(Solution().uniquePathsWithObstacles(
        obstacleGrid=[
            [0, 1],
            [0, 0]
        ]))

    print(Solution().uniquePathsWithObstacles(
        obstacleGrid=[
            [1],
        ]))


if __name__ == '__main__':
    test()
