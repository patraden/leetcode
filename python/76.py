class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        res = ""
        if m > n:
            return res

        tu = {}
        for c in t:
            tu[c] = tu.get(c, 0) + 1

        l, r = m, n + 1

        while l < r:
            m = (l + r) // 2

            flag = False
            prefix = {}

            for i in range(m):
                prefix[s[i]] = prefix.get(s[i], 0) + 1

            if self.includes(prefix, tu):
                r = m
                res = s[:m]
                continue

            for i in range(m, n):
                prefix[s[i]] = prefix.get(s[i], 0) + 1
                prefix[s[i - m]] -= 1
                if prefix[s[i - m]] == 0:
                    del prefix[s[i - m]]
                if self.includes(prefix, tu):
                    flag = True
                    res = s[i + 1 - m:i + 1]
                    break

            if flag:
                r = m
            else:
                l = m + 1
        return res

    def includes(self, this: dict, other: dict) -> bool:
        """ this contains other """
        for key in other:
            if key not in this or other[key] > this[key]:
                return False
        return True


def test():
    s = Solution()
    assert s.minWindow(s="a", t="aa") == ""
    assert s.minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert s.minWindow(s="a", t="a") == "a"
    assert s.minWindow(s="ADOBECODEBANC", t="ABB") == "BECODEBA"


if __name__ == "__main__":
    test()
