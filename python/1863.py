from typing import List
from functools import reduce
from itertools import combinations
from operator import xor


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        s = reduce(xor, nums)
        res = 0
        res += s

        if n % 2 == 0:
            for t in combinations(nums, n // 2):
                res += reduce(xor, t)
            n -= 1

        for k in range(1, n // 2 + 1):
            for t in combinations(nums, k):
                e = reduce(xor, t)
                res += e
                res += (e ^ s)

        return res


def test():
    print(Solution().subsetXORSum(nums=[1, 3]))
    print(Solution().subsetXORSum(nums=[5, 1, 6]))
    print(Solution().subsetXORSum(nums=[3, 4, 5, 6, 7, 8]))


if __name__ == '__main__':
    test()
