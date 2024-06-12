from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        p = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 2:
                nums[p], nums[i] = nums[i], nums[p]
                p -= 1

        print(nums)


def test():
    Solution().sortColors(nums=[2, 0, 2, 1, 1, 0])
    Solution().sortColors(nums=[2, 0, 1])
    Solution().sortColors(nums=[1, 0, 1, 2, 1])
    Solution().sortColors(nums=[2, 2, 1, 2, 1])
    Solution().sortColors(nums=[2, 2, 1, 2, 2])


if __name__ == '__main__':
    test()
