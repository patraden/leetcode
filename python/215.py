from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h, -num)
        i = 0
        elem = None
        while i < k:
            elem = heapq.heappop(h)
            i += 1
        if elem is not None:
            return -elem


def test():
    print(Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
    print(Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
    print(Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=0))


if __name__ == '__main__':
    test()
