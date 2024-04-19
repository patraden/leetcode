from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            nonlocal grid, visited, n, m
            visited.add((i, j))
            for (r, c) in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= r < n and 0 <= c < m and (r, c) not in visited and grid[r][c] == '1':
                    dfs(r, c)

        n, m = len(grid), len(grid[0])
        visited = set()
        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    res += 1
        return res


def test():
    print(Solution().numIslands(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))

    print(Solution().numIslands(grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))

    print(Solution().numIslands(grid=[
        ["1", "0", "1", "1", "1"],
        ["1", "1", "0", "1", "1"],
        ["1", "0", "1", "0", "0"],
        ["0", "0", "1", "1", "1"]
    ]))

    print(Solution().numIslands(grid=[
        ["1", "0", "1", "1", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "1", "1", "0", "1"]
    ]))


if __name__ == '__main__':
    test()
