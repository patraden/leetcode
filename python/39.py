from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i=0, prefix=None):
            nonlocal res, n
            prefix = prefix or []

            if sum(prefix) > target:
                return

            if sum(prefix) == target:
                res.append(prefix.copy())
                return

            for j in range(i, n):
                prefix.append(candidates[j])
                helper(j, prefix)
                prefix.pop()

        n = len(candidates)
        res = []
        helper()
        return res


def test():
    print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
    print(Solution().combinationSum(candidates=[2, 3, 5], target=8))
    print(Solution().combinationSum(candidates=[2], target=1))


if __name__ == '__main__':
    test()
