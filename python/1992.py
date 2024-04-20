from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n, m = len(land), len(land[0])
        land.append([0] * m)

        active_cols = {}
        res = []

        for i in range(n + 1):
            col = None
            for j in range(m):
                if land[i][j] == 1 and col is None:
                    [_, col, _] = active_cols.setdefault(j, [i, j, j])

                if col is not None and land[i][j] == 0:
                    active_cols[col][2] = j - 1
                    col = None

                if col is not None and land[i][j] == 1 and j == m - 1:
                    active_cols[col][2] = j

                if land[i][j] == 0 and j in active_cols:
                    [r, s, e] = active_cols[j]
                    res.append([r, s, i - 1, e])
                    del active_cols[j]
        return res


def test():
    print(Solution().findFarmland(land=[
        [1, 0, 0],
        [0, 1, 1],
        [0, 1, 1]
    ]))

    print(Solution().findFarmland(land=[
        [1, 1],
        [1, 1]
    ]))

    print(Solution().findFarmland(land=[
        [1, 1, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 1, 1, 1]
    ]))


if __name__ == '__main__':
    test()
