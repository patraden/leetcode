from typing import List


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        n = len(s)
        costs = [0] + [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        dp = [(0, 0)] * (n + 1)

        for i in range(n):
            j, cost = dp[i]
            cost += costs[i + 1]
            k = j
            while cost > maxCost:
                cost -= costs[k]
                k += 1
            dp[i + 1] = (k + 1 if k == 0 else k, cost)

        res = 0
        for i in range(1, n + 1):
            res = max(res, i - dp[i][0] + 1)

        return res


def test():
    # Solution().equalSubstring(s="abcd", t="bcdf", maxCost=3)
    Solution().equalSubstring(s="abcd", t="cdef", maxCost=3)
    # Solution().equalSubstring(s="cbcd", t="acce", maxCost=0)


if __name__ == '__main__':
    test()
