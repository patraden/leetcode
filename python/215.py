from typing import List



class Solution:
    # def findKthLargest(self, nums, k):
    #     if not nums: return
    #     pivot = random.choice(nums)
    #     left = [x for x in nums if x > pivot]
    #     mid = [x for x in nums if x == pivot]
    #     right = [x for x in nums if x < pivot]
    #
    #     L, M = len(left), len(mid)
    #
    #     if k <= L:
    #         return self.findKthLargest(left, k)
    #     elif k > L + M:
    #         return self.findKthLargest(right, k - L - M)
    #     else:
    #         return mid[0]
    def partitioning(self, a, lo, hi):
        import random
        if lo == hi:
            return lo

        i = lo
        # pivot = a[hi]
        pivot_idx = random.randint(lo, hi)
        pivot = a[pivot_idx]
        a[pivot_idx], a[hi] = a[hi], a[pivot_idx]

        for j in range(lo, hi):
            if a[j] < pivot:
                a[j], a[i] = a[i], a[j]
                i += 1
        a[hi], a[i] = a[i], a[hi]
        return i

    def findKthLargest(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            idx = self.partitioning(nums, lo, hi)
            if idx == len(nums) - k:
                return nums[idx]
            elif idx > len(nums) - k:
                hi = idx - 1
            else:
                lo = idx + 1


def test():
    print(Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=1))
    print(Solution().findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))


if __name__ == '__main__':
    test()
