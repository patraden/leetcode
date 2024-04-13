from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        res = 0

        matrix.append(['0'] * m)
        stacks = [[] for _ in range(m)]

        for i in range(n + 1):
            prefix = 0
            for j in range(m):
                if matrix[i][j] == "0":
                    prefix = 0
                else:
                    prefix += 1
                matrix[i][j] = prefix

                stack = stacks[j]
                while stack and matrix[stack[-1][0]][j] >= matrix[i][j]:
                    (idx, li) = stack.pop()
                    res = max((i - li - 1) * matrix[idx][j], res)
                li = -1 if not stack else stack[-1][0]
                stack.append((i, li))
        return res


def main():
    matrix1 = [["1", "0", "1", "1", "0"],
               ["1", "0", "1", "1", "1"],
               ["1", "1", "1", "1", "1"],
               ["1", "0", "1", "1", "0"]]
    matrix2 = [["0", "1", "1", "1", "1", "1", "1"]]

    print(Solution().maximalRectangle(matrix1))
    print(Solution().maximalRectangle(matrix2))


if __name__ == "__main__":
    main()
