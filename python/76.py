class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        res = ""
        if m > n:
            return res

        tu = {}
        for c in t:
            tu[c] = tu.get(c, 0) + 1

        l, r = 0, 0
        su = {}
        #  move right index first
        while not self.includes(su, tu):
            if r == n:
                return res
            su[s[r]] = su.get(s[r], 0) + 1
            r += 1

        res = s[:r]

        while l < r < n + 1:
            #  push left index to the right as much as possible
            while l < r:
                su[s[l]] -= 1
                if su[s[l]] == 0:
                    del su[s[l]]
                if not self.includes(su, tu):
                    # revert changes
                    su[s[l]] = su.get(s[l], 0) + 1
                    break
                l += 1
                if len(res) > (r - l):
                    res = s[l:r]
            # move right index to 1 position
            if r < n:
                su[s[r]] = su.get(s[r], 0) + 1
            r += 1
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
    assert s.minWindow(s="ADOBECODEBANC", t="DBC") == "DOBEC"


if __name__ == "__main__":
    test()
