from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]] # curr longest increasing subsequence
        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else: #
                j = bisect_left(sub, nums[i])
                sub[j] = nums[i]
        return len(sub)


def test():
    print(Solution().lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
    print(Solution().lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]))
    print(Solution().lengthOfLIS(nums=[-1]))


if __name__ == '__main__':
    test()
