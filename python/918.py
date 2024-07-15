from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        pres = nres = pprev = nprev = nums[0]
        s = sum(nums)

        for i in range(1, len(nums)):
            pcur = nums[i] if pprev + nums[i] < nums[i] else pprev + nums[i]
            ncur = nums[i] if nprev + nums[i] > nums[i] else nprev + nums[i]
            pres = max(pcur, pres)
            nres = min(ncur, nres)
            pprev = pcur
            nprev = ncur

        if nres != s:
            return max(pres, s - nres)
        return pres


def test():
    print(Solution().maxSubarraySumCircular([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7
    print(Solution().maxSubarraySumCircular(nums=[1, -2, 2, -2, 3]))  # 4
    print(Solution().maxSubarraySumCircular(nums=[1, -2, 3, -2]))  # 3
    print(Solution().maxSubarraySumCircular(nums=[5, -3, 5]))  # 10
    print(Solution().maxSubarraySumCircular(nums=[5]))  # 5
    print(Solution().maxSubarraySumCircular(nums=[-3, -2, -3]))  # -2
    print(Solution().maxSubarraySumCircular(nums=[-2, 4, -5, 4, -5, 9, 4]))  # 15
    print(Solution().maxSubarraySumCircular(nums=[0, 5, 8, -9, 9, -7, 3, -2]))  # 16
    print(Solution().maxSubarraySumCircular(
        nums=[-9, 14, 24, -14, 12, 18, -18, -10, -10, -23, -2, -23, 11, 12, 18, -9, 9, -29, 12, 4, -8, 15, 11, -12, -16,
              -9, 19, -12, 22, 16]))  # 99


if __name__ == '__main__':
    test()
