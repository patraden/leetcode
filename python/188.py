from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n

        for t in range(k):
            dp_next = [0] * n
            diff = float('-inf')
            for i in range(1, n):
                diff = max(diff, dp[i - 1] - prices[i - 1])
                dp_next[i] = max(dp_next[i - 1], prices[i] + diff)
            dp = dp_next.copy()

        return dp[n - 1]


def test():
    print(Solution().maxProfit(k=2, prices=[2, 4, 1]))
    print(Solution().maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))


if __name__ == '__main__':
    test()
