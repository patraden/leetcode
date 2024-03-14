from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        dp = [0] * len(prices)  # dp[i] - max profit if we sell on day i
        mn = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - mn)
            mn = min(mn, prices[i])
            dp[i] = res

        res = 0
        rdp = [0] * len(prices)  # rdp[i] - max negative profit if we sell on day i (reverse track)
        mx = prices[-1]
        for i in range(len(prices) - 1, 0, -1):
            res = min(res, prices[i] - mx)
            mx = max(mx, prices[i])
            rdp[i] = res

        res = 0
        for i in range(len(prices)):
            res = max(res, dp[i] - rdp[i])

        return res


def test():
    print(Solution().maxProfit(prices=[3, 3, 5, 0, 0, 3, 1, 4]))
    print(Solution().maxProfit(prices=[1, 2, 3, 4, 5]))
    print(Solution().maxProfit(prices=[7, 6, 4, 3, 1]))
    print(Solution().maxProfit(prices=[7]))


if __name__ == '__main__':
    test()
