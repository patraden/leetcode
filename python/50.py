from functools import lru_cache


class Solution:
    @lru_cache()
    def myPow(self, x: float, n: int) -> float:
        res = pow(x, n // 2) * pow(x, n // 2)
        if n % 2 == 1:
            return res * x
        return res


def test():
    # print(Solution().myPow(x=2.00000, n=10))
    # print(Solution().myPow(x=2.10000, n=3))
    # print(Solution().myPow(x=2.00000, n=-2))
    print(Solution().myPow(x=100, n=2**20 - 1))


if __name__ == '__main__':
    test()
