from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [-1] * amount
        for s in range(1, amount + 1):
            values = [dp[s - coin] for coin in coins if (s - coin) >= 0 and dp[s - coin] != -1]
            if values:
                dp[s] = min(values) + 1
        return dp[amount]


def test():
    print(Solution().coinChange(coins=[1, 2, 5], amount=11))
    print(Solution().coinChange(coins=[2], amount=3))
    print(Solution().coinChange(coins=[1], amount=0))


if __name__ == '__main__':
    test()
