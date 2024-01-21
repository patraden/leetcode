from typing import List


class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        _min = None
        for _, v in d.items():
            if not _min:
                _min = v
            else:
                _min = min(_min, v)

        for x in range(_min, 0, -1):
            res, finished = 0, True
            for _, v in d.items():
                g = self.groups(v, x)
                if not g:
                    finished = False
                    break
                res += g

            if finished:
                return res

    def groups(self, num, x):
        a = num // (x + 1)
        b = num % (x + 1)
        if b == 0:
            return a
        if a < (x - b):
            return None
        return a - (x - b) + (x - b + 1)


def test():
    assert Solution().minGroupsForValidAssignment(nums=[3, 2, 3, 2, 3]) == 2
    assert Solution().minGroupsForValidAssignment(nums=[10, 10, 10, 3, 1, 1]) == 4
    assert Solution().minGroupsForValidAssignment(nums=[1, 1, 1]) == 1
    assert Solution().minGroupsForValidAssignment(nums=[1, 1, 3, 3, 1, 1, 2, 2, 3, 1, 3, 2]) == 5


if __name__ == '__main__':
    test()
