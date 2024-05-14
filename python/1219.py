from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        res = 0

        def backtrack(r, c, path):
            nonlocal res

            cells = []
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                cr, cc = (r + dr, c + dc)
                if (cr, cc) not in visited and 0 <= cr < n and 0 <= cc < m and grid[cr][cc] > 0:
                    cells.append((cr, cc))

            if not cells:
                res = max(res, path)
                return

            for cr, cc in cells:
                visited.add((cr, cc))
                path += grid[cr][cc]
                backtrack(cr, cc, path)
                visited.remove((cr, cc))
                path -= grid[cr][cc]

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    visited.add((i, j))
                    backtrack(i, j, grid[i][j])
                    visited.remove((i, j))

        return res


def test():
    print(Solution().getMaximumGold(grid=[
        [0, 6, 0],
        [5, 8, 7],
        [0, 9, 0]
    ]))

    print(Solution().getMaximumGold(grid=[
        [1, 0, 7],
        [2, 0, 6],
        [3, 4, 5],
        [0, 3, 0],
        [9, 0, 20]
    ]))

    print(Solution().getMaximumGold(grid=[
        [0, 3, 1, 0, 8],
        [0, 3, 0, 4, 8],
    ]))


if __name__ == '__main__':
    test()
