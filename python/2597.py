from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def helper(i=0, prefix=None):
            nonlocal res, nums
            prefix = prefix or {}
            for j in range(i, len(nums)):
                if (nums[j] - k) not in prefix:
                    res += 1
                    prefix[nums[j]] = prefix.get(nums[j], 0) + 1
                    helper(j + 1, prefix)
                    prefix[nums[j]] -= 1
                    if prefix[nums[j]] == 0:
                        del prefix[nums[j]]

        nums.sort()
        res = 0
        helper()
        return res


def test():
    print(Solution().beautifulSubsets(nums=[2, 6, 4], k=2))
    print(Solution().beautifulSubsets(nums=[1], k=1))
    print(Solution().beautifulSubsets(nums=[11, 2, 6, 4, 8], k=2))
    print(Solution().beautifulSubsets(nums=[10, 4, 5, 7, 2, 1], k=3))


if __name__ == '__main__':
    test()
