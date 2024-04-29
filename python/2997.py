from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = 0
        for num in nums:
            s ^= num
        s ^= k
        return bin(s).count('1')


def test():
    print(Solution().minOperations(nums=[2, 1, 3, 4], k=1))
    print(Solution().minOperations(nums=[2, 0, 2, 0], k=0))


if __name__ == '__main__':
    test()
