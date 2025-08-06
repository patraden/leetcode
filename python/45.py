from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        mx = 0
        n = len(nums)
        dp = [n] * n
        dp[0] = 0

        for i, num in enumerate(nums):
            if i + num > mx:
                for j in range(mx + 1, min(i + num + 1, n)):
                    dp[j] = min(dp[j], dp[i] + 1)
                if i + num + 1 >= n:
                    break
                mx = i + num
                print(i, i + num, dp.copy(), mx)

        return dp[n - 1]


def test():
    Solution().jump(nums=[2, 3, 1, 1, 4])


if __name__ == '__main__':
    test()
