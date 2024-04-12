from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        lm, rm = height[0], height[n-1]
        li, ri = 1, n - 2
        res = 0

        while li <= ri:
            if lm <= rm:
                res += max(0, lm - height[li])
                lm = max(height[li], lm)
                li += 1
            else:
                res += max(0, rm - height[ri])
                rm = max(height[ri], rm)
                ri -= 1

        return res


    # def trap(self, height: List[int]) -> int:
    #     res, stack = 0, []
    #     for i in range(len(height)):
    #         while stack and height[stack[-1]] <= height[i]:
    #             k = stack.pop()
    #             if stack:
    #                 h = min(height[i], height[stack[-1]])
    #                 res += (h - height[k]) * (i - stack[-1] - 1)
    #         stack.append(i)
    #     return res




def main():
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap([4, 2, 0, 3, 2, 5]))
    print(Solution().trap([11 , 2, 33]))


if __name__ == "__main__":
    main()
