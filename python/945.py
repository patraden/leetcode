from typing import List
from collections import Counter


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        acc = Counter(nums)
        pointers = []
        pidx = 0
        res = 0

        for i in range(min(acc), max(acc) + 1):
            if i in acc:
                acc[i] -= 1
                if acc[i] > 0:
                    pointers.append(i)
            elif len(pointers) > 0 and pidx < len(pointers):
                start = pointers[pidx]
                if acc[start] > 0:
                    res += i - start
                    acc[start] -= 1
                if acc[start] == 0:
                    pidx += 1
        for i in range(max(acc) + 1, max(acc) + 1 + acc.total()):
            start = pointers[pidx]
            if acc[start] > 0:
                res += i - start
                acc[start] -= 1
            if acc[start] == 0:
                pidx += 1

        return res


def test():
    print(Solution().minIncrementForUnique(nums=[1, 2, 2]))
    print(Solution().minIncrementForUnique(nums=[3, 2, 1, 2, 1, 7]))
    print(Solution().minIncrementForUnique(nums=[4, 4, 7, 5, 1, 9, 4, 7, 3, 8]))


if __name__ == '__main__':
    test()
