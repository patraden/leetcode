from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = bisect_left(a=nums, x=target)
        hi = bisect_right(a=nums, x=target)
        if lo < len(nums) and nums[lo] == target:
            return [lo, hi - 1]
        return [-1, -1]

    def left_most(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums)

        while lo < hi:
            m = (lo + hi) // 2
            if nums[m] < target:
                lo = m + 1
            else:
                hi = m
        return lo

    def right_most(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums)

        while lo < hi:
            m = (lo + hi) // 2
            if target < nums[m]:
                hi = m
            else:
                lo = m + 1
        return lo


def test():
    kwargs = {
        # "nums": [5, 7, 7, 8, 8, 10],
        "nums": [6, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9],
        "target": 8
    }
    # print(Solution().left_most(**kwargs))
    print(Solution().searchRange(**kwargs))
    print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))


if __name__ == '__main__':
    test()
