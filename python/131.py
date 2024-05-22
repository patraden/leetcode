from typing import List
from functools import cache


class Solution:
    @cache
    def is_palindrome(self, s: str, i, j) -> bool:
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        prefix = []
        res = []

        def helper(k):
            if k >= len(s):
                res.append(prefix.copy())
                return
            for i in range(k, len(s)):
                if self.is_palindrome(s, k, i):
                    prefix.append(s[k:i + 1])
                    helper(i + 1)
                    prefix.pop()

        helper(0)
        return res


def test():
    print(Solution().partition('a'))
    print(Solution().partition('aab'))
    print(Solution().partition('aabaab'))


if __name__ == '__main__':
    test()
