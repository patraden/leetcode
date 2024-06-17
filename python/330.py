from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        m = 1
        i = res = 0
        while m <= n:
            if i < len(nums) and nums[i] <= m:
                m += nums[i]
                i += 1
            else:
                m += m
                res += 1
        return res


def test():
    print(Solution().minPatches(nums=[1], n=1))
    print(Solution().minPatches(nums=[1,3], n=6))
    print(Solution().minPatches(nums=[1, 5, 10], n=20))
    print(Solution().minPatches(nums=[1, 2, 3, 4], n=32))
    print(Solution().minPatches(nums=[1, 2, 2, 5, 5, 5, 7], n=5))
    print(Solution().minPatches(nums=[1, 2, 2], n=5))
    print(Solution().minPatches(nums=[], n=15))
    print(Solution().minPatches(nums=[1, 2, 2, 6, 34, 38, 41, 44, 47, 47, 56, 59, 62, 73, 77, 83, 87, 89, 94], n=20))
    print(Solution().minPatches(nums=[1, 2, 2, 6], n=20))
    print(Solution().minPatches(nums=[2, 9, 22, 28, 31, 38, 44, 44, 47, 52, 56, 61, 71, 77], n=42))
    print(Solution().minPatches(nums=[1, 2, 16, 19, 31, 35, 36, 64, 64, 67, 69, 71, 73, 74, 76, 79, 80, 91, 95, 96, 97],
                                n=8))


if __name__ == '__main__':
    test()
