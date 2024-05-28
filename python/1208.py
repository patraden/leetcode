class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = cost = res = 0
        for i in range(len(s)):
            cost += abs(ord(s[i]) - ord(t[i]))
            while cost > maxCost:
                cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            res = max(res, i - start + 1)
        return res


def test():
    print(Solution().equalSubstring(s="abcd", t="bcdf", maxCost=3))
    print(Solution().equalSubstring(s="abcd", t="cdef", maxCost=3))
    print(Solution().equalSubstring(s="cbcd", t="acce", maxCost=0))


if __name__ == '__main__':
    test()
