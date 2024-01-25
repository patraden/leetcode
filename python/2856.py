from typing import List
import heapq


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        distinct, duplicates = [], []

        prev = None
        duplicates_indexes = []
        for curr in nums + [None]:
            if curr == prev:
                distinct[-1] += 1
                continue
            if distinct and distinct[-1] > 1:
                heapq.heappush(duplicates, (-distinct[-1], len(distinct) - 1))
                duplicates_indexes.append(len(distinct) - 1)
            distinct.append(1)
            prev = curr
        distinct.pop()

        # no duplicates is the simplest scenario
        if not duplicates_indexes:
            return len(distinct) % 2

        end_idx = None
        for idx in duplicates_indexes:
            while distinct[idx] > 1 and duplicates:
                top_freq, top_idx = heapq.heappop(duplicates)
                if top_idx <= idx:
                    continue
                distinct[idx] -= 1
                distinct[top_idx] -= 1
                if -top_freq > 2:
                    heapq.heappush(duplicates, (top_freq + 1, top_idx))

            if not duplicates:
                end_idx = idx
                break

        if distinct[end_idx] >= len(distinct) - 1:
            return distinct[end_idx] - len(distinct) + 1
        else:
            return (len(distinct) - distinct[end_idx] + 1) % 2


def test():
    print(Solution().minLengthAfterRemovals(nums=[1, 1, 2]))
    print(Solution().minLengthAfterRemovals(nums=[1, 1, 2, 2, 2, 3, 3, 3, 3, 3]))
    print(Solution().minLengthAfterRemovals(nums=[1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4]))
    print(Solution().minLengthAfterRemovals(nums=[2, 3, 6, 9]))
    print(Solution().minLengthAfterRemovals(nums=[1, 2, 2, 2, 3, 3]))


if __name__ == '__main__':
    test()
