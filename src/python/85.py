from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0]) if len(matrix) > 0 else 0
        matrix_hist = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            count_one = 0
            for j in range(m):
                if matrix[i][j] == "0":
                    matrix_hist[j][i] = 0
                    count_one = 0
                else:
                    count_one += 1
                    matrix_hist[j][i] = count_one

        _max = 0
        for row in matrix_hist:
            _max = max(_max, self.largestRectangleArea(row))

        return _max

    def largestRectangleArea(self, heights: list[int]):
        n = len(heights)
        left = [0] * n
        stack = [-1]
        for i in range(n):
            idx = stack[-1]
            while idx != -1 and heights[idx] >= heights[i]:
                stack.pop()
                idx = stack[-1]
            left[i] = idx
            stack.append(i)

        right = [0] * n
        stack = [n]
        for i in range(n - 1, -1, -1):
            idx = stack[-1]
            while idx != n and heights[idx] >= heights[i]:
                stack.pop()
                idx = stack[-1]
            right[i] = idx
            stack.append(i)

        res = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            res = max(res, heights[i] * width)

        return res


def main():
    matrix1 = [["1", "0", "1", "0", "0"],
               ["1", "0", "1", "1", "1"],
               ["1", "1", "1", "1", "1"],
               ["1", "0", "0", "1", "0"]]
    matrix2 = [["1"]]

    print(Solution().maximalRectangle(matrix1))
    print(Solution().maximalRectangle(matrix2))


if __name__ == "__main__":
    main()
