from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        l, r = 0, n * m
        while l < r:
            mid = (l + r) // 2
            if matrix[mid // m][mid % m] == target:
                return True
            elif target < matrix[mid // m][mid % m]:
                r = mid
            else:
                l = mid + 1
        return False


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(Solution().searchMatrix(matrix, target))


if __name__ == "__main__":
    main()
