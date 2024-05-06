from typing import List
from itertools import accumulate
from bisect import bisect_left


class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)  # length of the result
        idx = [0] * (n + 1)
        acc = list(accumulate(nums, initial=0))

        j = 0
        for i in range(1, n + 1):
            j = max(j, idx[i])
            dp[i] = dp[j] + 1
            k = bisect_left(acc, 2 * acc[i] - acc[j])
            if k < len(idx):
                idx[k] = i
        return dp[n]

        # for i in range(1, n + 1):
        #     if dp[i] == 0:
        #         dp[i] = dp[i - 1]
        #         vl[i] = vl[i - 1] + nums[i - 1]
        #
        #     target = vl[i] + prefixes[i]
        #     idx = bisect_left(prefixes, target)
        #     if idx < len(prefixes):
        #         dp[idx] = dp[i] + 1
        #         vl[idx] = prefixes[idx] - prefixes[i]
        #
        # print(dp)
        # return dp[n]


def test():
    print(Solution().findMaximumLength(nums=[4, 3, 2, 6]))
    # print(Solution().findMaximumLength(nums=[1, 2, 3, 4]))
    # print(Solution().findMaximumLength(nums=[5, 2, 2]))
    # print(Solution().findMaximumLength(nums=[20]))
    # print(Solution().findMaximumLength(nums=[272, 482, 115, 925, 983]))
    # print(Solution().findMaximumLength(
    #     nums=[908, 906, 819, 716, 609, 317, 172, 886, 718, 511, 215, 448, 356, 335, 856, 618, 127, 107, 859, 217, 821,
    #           505, 646, 155, 917, 445, 28, 919, 503, 687, 247, 876, 216, 544, 709, 354, 834, 967, 799, 173, 163, 202,
    #           820, 144, 23, 658]))


if __name__ == '__main__':
    test()
