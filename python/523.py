from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        p = 0
        h = {p: -1}
        for i in range(len(nums)):
            num = nums[i]
            p += num
            p %= k
            if p in h and (i - h[p]) >= 2:
                return True
            h.setdefault(p, i)
        return False


def main():
    print(Solution().checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))
    print(Solution().checkSubarraySum([23, 2, 6, 4, 7], k=6))
    print(Solution().checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13))
    print(Solution().checkSubarraySum(nums=[4, 2, 5], k=7))


if __name__ == "__main__":
    main()
