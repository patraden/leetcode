from typing import List

def right_most_search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if target >= nums[m]:
            l = m + 1
        else:
            r = m
    return l


def left_most_search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if target > nums[m]:
            l = m + 1
        else:
            r = m - 1
    return r