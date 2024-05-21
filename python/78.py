from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(idx=0, prefix=None):
            prefix = prefix or []
            res.append(list(prefix))
            for i in range(idx, len(nums)):
                prefix.append(nums[i])
                helper(i + 1, prefix)
                prefix.pop()

        helper()
        return res


def test():
    print(Solution().subsets([1, 2]))


if __name__ == '__main__':
    test()
