from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]

        dp = [0] * n
        for row in grid:

            min1, min2 = None, None
            for i, num in enumerate(row):
                if min1 is None:
                    min1 = num + dp[i]
                    continue
                if min2 is None:
                    min2 = num + dp[i]
                if (num + dp[i]) <= min1:
                    min2 = min1
                    min1 = num + dp[i]
                elif (num + dp[i]) <= min2:
                    min2 = num + dp[i]

            for i, num in enumerate(row):
                dp[i] = min2 if (num + dp[i]) == min1 else min1

        return min(dp)


def test():
    print(Solution().minFallingPathSum(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(Solution().minFallingPathSum(grid=[[7]]))


if __name__ == '__main__':
    test()
