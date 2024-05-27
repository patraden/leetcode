from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        lo, hi = 0, len(nums)
        while lo < hi:
            mi = (lo + hi) // 2
            if nums[mi] == len(nums) - mi:
                if mi > 0 and nums[mi - 1] == nums[mi]:
                    return -1
                return len(nums) - mi
            elif nums[mi] < len(nums) - mi:
                lo = mi + 1
            else:
                hi = mi

        count = len(nums) - lo

        if 0 < lo < len(nums) and nums[lo] > count and nums[lo - 1] == count:
            return -1

        return count if count > 0 else -1


def test():
    print(Solution().specialArray(nums=[0]))
    print(Solution().specialArray(nums=[10]))
    print(Solution().specialArray(nums=[0, 0]))
    print(Solution().specialArray(nums=[3, 5]))
    print(Solution().specialArray(nums=[0, 4, 3, 0, 4]))
    print(Solution().specialArray(nums=[3, 6, 7, 7, 0]))
    print(Solution().specialArray(nums=[2, 3, 0, 2]))


if __name__ == '__main__':
    test()
