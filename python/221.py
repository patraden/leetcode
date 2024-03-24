from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        res = 0
        if m == 0:
            return res

        n = len(matrix[0])
        for j in range(n):
            matrix[0][j] = int(matrix[0][j])
            res = max(res, matrix[0][j])

        for i in range(m):
            matrix[i][0] = int(matrix[i][0])
            res = max(res, matrix[i][0])

        for i in range(1, m):
            for j in range(1, n):
                if int(matrix[i][j]) == 1:
                    matrix[i][j] = 1 + min(
                        int(matrix[i - 1][j - 1]),
                        int(matrix[i - 1][j]),
                        int(matrix[i][j - 1])
                    )
                    res = max(res, matrix[i][j])
                else:
                    matrix[i][j] = 0

        return res * res


def test():
    print(Solution().maximalSquare(
        matrix=[["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]]))

    print(Solution().maximalSquare(
        matrix=[["0", "1"], ["1", "0"]]))

    print(Solution().maximalSquare(
        matrix=[["0", "1", "1", "1", "1", "0"],
                ["0", "1", "1", "1", "1", "0"],
                ["0", "1", "1", "1", "1", "1"],
                ["0", "1", "1", "1", "1", "0"],
                ["0", "0", "0", "1", "1", "0"],
                ["0", "0", "1", "1", "1", "0"]
                ]))


if __name__ == '__main__':
    test()
