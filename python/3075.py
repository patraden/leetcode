from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        h = sorted(happiness, reverse=True)
        res = 0
        for d in range(k):
            v = h[d] - d
            if v <= 0:
                return res
            res += v
        return res


def test():
    print(Solution().maximumHappinessSum(happiness=[1, 2, 3], k=2))
    print(Solution().maximumHappinessSum(happiness=[1, 1, 1, 1], k=2))


if __name__ == '__main__':
    test()
