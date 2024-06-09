from typing import List
from collections import Counter


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        p = res = 0
        counter = Counter()
        counter[0] = 1

        for i in range(len(nums)):
            num = nums[i]
            p += num
            p %= k
            if counter[p]:
                res += counter[p]
            counter[p] += 1
        return res


def test():
    print(Solution().subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5))
    print(Solution().subarraysDivByK(nums=[5], k=9))


if __name__ == '__main__':
    test()
