from functools import lru_cache

class Solution:
    @lru_cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n in (1, 2):
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)


def test():
    n = 38
    for i in range(n):
        print(i, Solution().tribonacci(i))


if __name__ == '__main__':
    test()
