from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        s = sum(nums) % p
        if s == 0:
            return 0

        d = {0: [-1]}
        prefix = 0
        res = len(nums)

        for i, num in enumerate(nums):
            prefix += num
            prefix %= p
            d.setdefault(prefix, []).append(i)
            tail = (s - prefix) % p
            lead = p - tail if tail > 0 else 0
            if lead in d:
                sub = i - d[lead][-1]
                res = min(res, sub)
        return -1 if res == len(nums) else res


def test():
    assert Solution().minSubarray(nums=[10, 15, 4, 2, 5, 55], p=7) == 0
    assert Solution().minSubarray(nums=[6, 3, 5, 2], p=9) == 2
    assert Solution().minSubarray(nums=[3, 1, 4, 2], p=6) == 1
    assert Solution().minSubarray(nums=[1, 2, 3], p=3) == 0
    assert Solution().minSubarray(nums=[1, 12, 5, 11, 17, 34, 4], p=17) == 2


if __name__ == "__main__":
    test()
