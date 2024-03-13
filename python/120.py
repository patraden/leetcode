from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            row = triangle[i]
            m = len(row)
            triangle[i][0] += triangle[i - 1][0]
            for j in range(1, m - 1):
                triangle[i][j] = min(
                    triangle[i - 1][j] + triangle[i][j],
                    triangle[i - 1][j - 1] + triangle[i][j]
                )
            triangle[i][m - 1] += triangle[i - 1][m - 2]

        return min(triangle.pop())


def test():
    s = Solution()
    print(s.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print(s.minimumTotal(triangle=[[-10]]))


if __name__ == '__main__':
    test()
