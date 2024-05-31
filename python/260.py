from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num

        bit = x & -x
        res = [0, 0]

        for num in nums:
            if num & bit:
                res[0] ^= num
            else:
                res[1] ^= num

        return res


def test():
    print(Solution().singleNumber(nums=[1, 2, 1, 3, 2, 5]))


if __name__ == '__main__':
    test()
