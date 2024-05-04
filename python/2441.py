from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = set()
        res = None
        for num in nums:
            if num in d:
                res = abs(num) if res is None else max(res, abs(num))
            d.add(-num)
        return res if res else -1


def test():
    print(Solution().findMaxK(nums=[-1, 2, -3, 3]))
    print(Solution().findMaxK(nums=[-1, 10, 6, 7, -7, 1, -10, 7]))
    print(Solution().findMaxK(nums=[-10, 8, 6, 7, -2, -3]))


if __name__ == '__main__':
    test()
