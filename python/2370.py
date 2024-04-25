from typing import List


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = {}
        res = 0
        for c in s:
            c = ord(c)
            prev = 0
            for b in range(max(ord('a'), c - k), min(ord('z'), c + k) + 1):
                prev = max(prev, dp.setdefault(b, 0))
            dp[c] = prev + 1
            res = max(res, dp[c])
        return res


def test():
    print(Solution().longestIdealString(s="acfgbd", k=2))
    print(Solution().longestIdealString(s="abcd", k=1))
    print(Solution().longestIdealString(s="cgftnmbdts", k=1))


if __name__ == '__main__':
    test()
