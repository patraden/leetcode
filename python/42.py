from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res, stack = 0, []
        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                k = stack.pop()
                if stack:
                    h = min(height[i], height[stack[-1]])
                    res += (h - height[k]) * (i - stack[-1] - 1)
            stack.append(i)
        return res


def main():
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap([4, 2, 0, 3, 2, 5]))


if __name__ == "__main__":
    main()
