from typing import List
from functools import reduce


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:

        bit = 1 << len(nums) - 1
        mn_bit = 1 << k - 1
        nms = int(reduce(lambda x, y: x + str(y), nums, ""), 2)

        mask = 1
        for _ in range(k - 1):
            mask <<= 1
            mask += 1
        mask <<= len(nums) - k

        res = 0
        while bit >= mn_bit:
            if not bit & nms:
                nms ^= mask
                res += 1
            bit >>= 1
            mask >>= 1

        if nms == int("1" * len(nums), 2):
            return res
        return -1


def test():
    print(Solution().minKBitFlips(nums=[0, 1, 0], k=1))
    print(Solution().minKBitFlips(nums=[1, 1, 0], k=2))
    print(Solution().minKBitFlips(nums=[0, 0, 0, 1, 0, 1, 1, 0], k=3))


if __name__ == '__main__':
    test()
