from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2


def test():
    print(Solution().singleNumber(nums=[2, 2, 3, 2]))
    print(Solution().singleNumber(nums=[0, 1, 0, 1, 0, 1, 99]))


if __name__ == '__main__':
    test()
