from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []
        right, down, left, up = 0, 1, 2, 3

        def helper(r, c, n, m, direction: int):
            nonlocal ans, matrix
            if n <= 0 or m <= 0:
                return

            if direction == right:
                for j in range(c, c + m):
                    ans.append(matrix[r][j])
                helper(r + 1, c + m - 1, n - 1, m, down)

            if direction == down:
                for i in range(r, r + n):
                    ans.append(matrix[i][c])
                helper(r + n - 1, c - 1, n, m - 1, left)

            if direction == left:
                for j in range(c, c - m, -1):
                    ans.append(matrix[r][j])
                helper(r - 1, c - m + 1, n - 1, m, up)

            if direction == up:
                for i in range(r, r - n, -1):
                    ans.append(matrix[i][c])
                helper(r - n + 1, c + 1, n, m - 1, right)

        helper(0, 0, len(matrix), len(matrix[0]), right)

        return ans


def test():
    # print(Solution().spiralOrder(matrix=[
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]))

    print(Solution().spiralOrder(matrix=[
        [1, 2, 3, 4],
        # [4, 5, 6, 5],
        # [4, 5, 6, 5],
        # [4, 5, 6, 5],
        # [4, 5, 6, 5],
        # [7, 8, 9]
    ]))

    print(Solution().spiralOrder(matrix=[
        [1, 2],
        [4, 4],
        [7, 8]
    ]))


if __name__ == '__main__':
    test()
