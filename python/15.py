from typing import List
from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res = set()

        for key in counter.keys():
            if key == 0 and counter[key] > 2:
                res.add((key, key, key))
            if key != 0 and key % 2 == 0 and counter[-(key // 2)] > 1:
                res.add((-(key // 2), -(key // 2), key))

        nums = list(set(nums))
        target = 0

        for i in range(len(nums)):
            h = {}
            for j in range(i + 1, len(nums)):
                if target - nums[j] in h:
                    for (k, m) in h[target - nums[j]]:
                        res.add(tuple(sorted((nums[k], nums[m], nums[j]))))
                else:
                    s = nums[i] + nums[j]
                    h.setdefault(s, []).append((i, j))

        return [[i, j, k] for (i, j, k) in res]


def test():
    print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum(nums=[0, 1, 1]))
    print(Solution().threeSum(nums=[0, 0, 0]))
    print(Solution().threeSum(nums=[-1, 0, 1, 0]))


if __name__ == '__main__':
    test()
