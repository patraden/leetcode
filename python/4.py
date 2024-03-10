from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # assume nums1 not less than nums2
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        if n == m == 0:
            return

        k = (n + m) // 2

        l, r = k - m, k
        while l < r:
            mid = (l + r) // 2
            if nums1[mid] - nums2[k - mid - 1] <= 0:
                l = mid + 1
            else:
                r = mid

        nums1_nxt = nums2_nxt = float('inf')
        if 0 <= l < n:
            nums1_nxt = nums1[l]
        if 0 <= k - l < m:
            nums2_nxt = nums2[k - l]
        nxt = min(nums1_nxt, nums2_nxt)

        nums1_prv = nums2_prv = float('-inf')
        if 0 <= l - 1 < n:
            nums1_prv = nums1[l - 1]
        if 0 <= k - l - 1 < m:
            nums2_prv = nums2[k - l - 1]
        prv = max(nums1_prv, nums2_prv)

        if (n + m) % 2 == 1:
            return nxt
        else:
            return (nxt + prv) / 2


def test():
    s = Solution()
    print(s.findMedianSortedArrays(nums1=[-110], nums2=[100, 110, 112]))


if __name__ == '__main__':
    test()
