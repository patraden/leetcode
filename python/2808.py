from typing import List


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)

        for i, num in enumerate(nums):
            if num in d:
                si, ei, _max = d[num]
                d[num][1] = i
                d[num][2] = max(_max, (i - ei - 1))
            else:
                d[num] = [i, i, 0]  # first, last, max

        ans = n - 1
        for num in d:
            si, ei, _max = d[num]
            _max = max(_max, (si - ei - 1) % n)
            ans = min(ans, _max)

        return ans // 2 + ans % 2


def test():
    assert Solution().minimumSeconds(nums=[1, 2, 1, 2]) == 1
    assert Solution().minimumSeconds(nums=[2, 1, 3, 3, 2]) == 2
    assert Solution().minimumSeconds(nums=[5, 5, 5, 5]) == 0


if __name__ == '__main__':
    test()
