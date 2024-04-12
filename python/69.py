class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0

        l, r = 1, x
        while l <= r:
            m = (l + r) // 2
            if m * m > x:
                r = m - 1
            else:
                l = m + 1

        return r


def test():
    print(Solution().mySqrt(x=2**31-1))
    print(Solution().mySqrt(x=8))
    print(Solution().mySqrt(x=19 * 19), )


if __name__ == '__main__':
    test()
