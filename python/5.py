class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, prv = len(s), [True]
        res = s[n - 1:]

        for i in range(n - 2, -1, -1):
            cur = [False] * (len(prv) + 1)
            for k in range(len(cur)):
                j = i + k
                cur[k] = (
                    i == j or
                    (i + 1 == j and s[i] == s[j]) or
                    (i + 1 < j and prv[k - 2] and s[i] == s[j])
                )
                if cur[k] and (k + 1) > len(res):
                    res = s[i:i + k + 1]
            prv = cur
        return res


def test():
    print(Solution().longestPalindrome(s="babad"))
    print(Solution().longestPalindrome(s="cbbd"))
    print(Solution().longestPalindrome("bbbabbbb"))
    print(Solution().longestPalindrome("bab"))
    print(Solution().longestPalindrome("b"))
    print(Solution().longestPalindrome("babdasaddddddddasadcccdaxx"))


if __name__ == '__main__':
    test()
