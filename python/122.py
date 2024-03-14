from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mn = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > mn:
                res += prices[i] - mn
                mn = prices[i]
                continue

            mn = min(mn, prices[i])
        return res


def test():
    print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit(prices=[1, 2, 3, 4, 5]))
    print(Solution().maxProfit(prices=[7, 6, 4, 3, 1]))
    print(Solution().maxProfit(prices=[7]))


if __name__ == '__main__':
    test()
