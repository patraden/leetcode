from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


def test():
    print(Solution().singleNumber(nums=[2, 2, 1]))
    print(Solution().singleNumber(nums=[4, 1, 2, 1, 2]))
    print(Solution().singleNumber(nums=[1]))


if __name__ == '__main__':
    test()
