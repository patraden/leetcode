from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        pprefix = 0
        prefix = (nums[0] + nums[1]) % k
        if prefix == 0:
            return True
        d = {pprefix}
        for i in range(2, len(nums)):
            prefix = (prefix + nums[i]) % k
            pprefix = (pprefix + nums[i - 2]) % k
            d.add(pprefix)
            if prefix in d:
                return True
        return False


def main():
    print(Solution().checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))
    print(Solution().checkSubarraySum([23, 2, 6, 4, 7], k=6))
    print(Solution().checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13))
    print(Solution().checkSubarraySum(nums=[4, 2, 5], k=7))


if __name__ == "__main__":
    main()
