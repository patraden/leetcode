from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid) - 1):
                if j == 1:
                    row = []
                mx = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        mx = max(mx, grid[i + di][j + dj])
                row.append(mx)
                if j == len(grid) - 2:
                    res.append(row)

        return res


def test():
    Solution().largestLocal(grid=[
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2]
    ])

    Solution().largestLocal(grid=[
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ])

    Solution().largestLocal(grid=[
        [1, 1, 2],
        [1, 122, 1],
        [1, 1, 11]
    ])


if __name__ == '__main__':
    test()
