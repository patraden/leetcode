from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)
        nums += [float('-inf')]
        while lo < hi:
            mi = (lo + hi) // 2
            # print(lo, hi, mi)
            if nums[mi] > nums[mi + 1]:
                hi = mi
            else:
                lo = mi + 1
        return lo


def test():
    print(Solution().findPeakElement(nums=[1, 2, 3, 1]))
    print(Solution().findPeakElement(nums=[1, 2, 3, 4, 5, 6]))
    print(Solution().findPeakElement(nums=[6, 5, 4, 3, 2, 1]))
    print(Solution().findPeakElement(nums=[6, 5, 2, 3, 2, 1]))
    print(Solution().findPeakElement(nums=[5, 6, 4]))
    print(Solution().findPeakElement(nums=[4]))


if __name__ == '__main__':
    test()
