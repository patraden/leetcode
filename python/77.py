from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(i=1, prefix=None):
            nonlocal res
            prefix = prefix or []

            if len(prefix) == k:
                res.append(prefix.copy())
                return

            for j in range(i, n + 1):
                prefix.append(j)
                helper(j + 1, prefix)
                prefix.pop()

        res = []
        helper()
        return res


def test():
    Solution().combine(20, 20)


if __name__ == '__main__':
    test()
