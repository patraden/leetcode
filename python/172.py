class Solution:
    def trailingZeroes(self, n: int) -> int:
        res, pow = 0, 5
        while pow <= n:
            res += n // pow
            pow *= 5
        return res



def test():
    print(Solution().trailingZeroes(n=3))
    print(Solution().trailingZeroes(n=5))
    print(Solution().trailingZeroes(n=30))
    print(Solution().trailingZeroes(n=50))


if __name__ == '__main__':
    test()
