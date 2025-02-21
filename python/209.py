from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        res = len(nums) + 1
        left = right = 0

        s = nums[0]
        while left <= right < len(nums):
            if s < target:
                right += 1
                if right < len(nums):
                    s += nums[right]
            else:
                res = min(res, right - left + 1)
                s -= nums[left]
                left += 1

        if res == len(nums) + 1:
            return 0

        return res


def test():
    s = Solution()
    print(s.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
    print(s.minSubArrayLen(target=4, nums=[1, 4, 4]))
    print(s.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))


if __name__ == '__main__':
    test()
