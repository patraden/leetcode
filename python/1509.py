from typing import List
import heapq


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums_size = len(nums)
        if nums_size <= 4:
            return 0

        # Find the four smallest elements
        smallest_four = sorted(heapq.nsmallest(4, nums))

        # Find the four largest elements
        largest_four = sorted(heapq.nlargest(4, nums))

        min_diff = float("inf")
        # Four scenarios to compute the minimum difference
        for i in range(4):
            min_diff = min(min_diff, largest_four[i] - smallest_four[i])

        return min_diff


def test():
    print(Solution().minDifference(nums=[1, 5, 0, 10, 14]))
    print(Solution().minDifference(nums=[9, 48, 92, 48, 81, 31]))


if __name__ == '__main__':
    test()
