from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        l = 0
        res = 1
        minq, maxq = deque([0]), deque([0])

        for i in range(1, len(nums)):
            # set right pointer to i
            while minq and nums[minq[-1]] > nums[i]:
                minq.pop()
            minq.append(i)
            while maxq and nums[maxq[-1]] < nums[i]:
                maxq.pop()
            maxq.append(i)

            # trying to shift right pointer
            while l < i and nums[maxq[0]] - nums[minq[0]] > limit:
                l += 1
                if minq[0] < l:
                    minq.popleft()
                if maxq[0] < l:
                    maxq.popleft()

            res = max(res, i - l + 1)
        return res


def test():
    print(Solution().longestSubarray(nums=[8, 2, 4, 7], limit=4))
    print(Solution().longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5))
    print(Solution().longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0))


if __name__ == '__main__':
    test()
