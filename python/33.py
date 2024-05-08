from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            m = (lo + hi) // 2

            if nums[m] == target:
                return m

            if nums[lo] <= nums[m]:  # left part is good
                if nums[lo] <= target < nums[m]:
                    hi = m - 1
                else:
                    lo = m + 1

            if nums[m] <= nums[hi]:  # right part is good
                if nums[m] < target <= nums[hi]:
                    lo = m + 1
                else:
                    hi = m - 1
        return -1


def test():
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], target=0))
    print(Solution().search([1, 2, 4, 5, 6, 7, 0], target=0))
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
    print(Solution().search(nums=[4], target=3))
    print(Solution().search(nums=[3, 2], target=3))
    print(Solution().search(nums=[3, 2], target=2))
    print(Solution().search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=8))


if __name__ == '__main__':
    test()
