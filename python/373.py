from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m, res = len(nums1), len(nums2), []
        pointers = [(nums1[0] + nums2[0], 0, 0)]
        idx = 0
        while idx < k:
            val, r, c = heapq.heappop(pointers)
            if c == 0 and r < n - 1:
                heapq.heappush(pointers, (nums1[r + 1] + nums2[c], r + 1, c))

            while c < m and idx < k and (not pointers or (nums1[r] + nums2[c]) <= pointers[0][0]):
                res.append([nums1[r], nums2[c]])
                c += 1
                idx += 1

            if c < m:
                heapq.heappush(pointers, (nums1[r] + nums2[c], r, c))

        return res


def test():
    print(Solution().kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
    print(Solution().kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))
    print(Solution().kSmallestPairs(nums1=[2], nums2=[3, 40], k=2))


if __name__ == '__main__':
    test()
