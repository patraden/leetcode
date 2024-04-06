class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + (dp[i - 2] if i - 2 >= 0 else 0)
        return dp[-1]


def test():
    print(Solution().climbStairs(1))
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))
    print(Solution().climbStairs(4))
    print(Solution().climbStairs(5))


if __name__ == '__main__':
    test()
