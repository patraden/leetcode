from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + (dp[i - 2] if i - 2 >= 0 else 0))
        return dp[-1]


def test():
    print(Solution().rob(nums=[1, 2, 3, 1]))
    print(Solution().rob(nums=[2, 7, 9, 3, 1]))


if __name__ == '__main__':
    test()
