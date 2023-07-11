from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(nums)):
            qty = 0
            while stack and nums[stack[-1][0]] <= nums[i]:
                j, j_qty = stack.pop()
                qty = max(qty, j_qty)
            if not stack:
                stack.append((i, 0))
            else:
                stack.append((i, qty + 1))
                res = max(res, qty + 1)
        return res


def main():
    print(Solution().totalSteps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]))
    print(Solution().totalSteps([4, 5, 7, 7, 13]))
    print(Solution().totalSteps([7, 14, 4, 14, 13, 2, 6, 13]))


if __name__ == "__main__":
    main()
