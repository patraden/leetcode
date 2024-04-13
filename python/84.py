from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n, stack = len(heights), []
        heights.append(float('-inf'))
        res = 0
        for i in range(n + 1):
            while stack and heights[stack[-1][0]] >= heights[i]:
                (idx, li) = stack.pop()
                res = max((i - li - 1) * heights[idx], res)
            li = -1 if not stack else stack[-1][0]
            stack.append((i, li))
        return res


def main():
    test1 = [2, 1, 5, 6, 2, 3]
    test2 = [2, 4]
    print(Solution().largestRectangleArea(test1))
    print(Solution().largestRectangleArea(test2))


if __name__ == "__main__":
    main()
