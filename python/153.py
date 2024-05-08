from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            if lo == hi or nums[lo] < nums[hi]:
                return nums[lo]

            mi = (lo + hi) // 2
            if nums[lo] <= nums[mi]:  # left part is good
                if nums[mi + 1] < nums[mi]:
                    return nums[mi + 1]
                lo = mi + 1

            if nums[mi] <= nums[hi]:  # right part is good
                if mi == lo or nums[mi - 1] > nums[mi]:
                    return nums[mi]
                hi = mi - 1


def test():
    # print(Solution().findMin([66, -22, -5, 33, 44, 55]))
    # print(Solution().findMin([33, 44, 55, 66, -22, -5]))

    # print(Solution().findMin([66, -22, -5]))

    nums = [-44, -33, -22, -5, 33, 44, 55]
    n = len(nums)
    for d in range(n):
        test_nums = [0] * n
        for i in range(n):
            test_nums[(i + d) % n] = nums[i]

        print(test_nums)
        print(Solution().findMin(test_nums))


if __name__ == '__main__':
    test()
