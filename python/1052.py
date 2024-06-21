from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(grumpy)
        prefix = [0]
        p = res = 0
        for i in range(n):
            if grumpy[i] == 1:
                p += customers[i]
            else:
                res += customers[i]
            prefix.append(p)

        mx = 0
        for i in range(minutes, n + 1):
            mx = max(mx, prefix[i] - prefix[i - minutes])

        return mx + res


def test():
    print(Solution().maxSatisfied(
        customers=[1, 0, 1, 2, 1, 1, 7, 5],
        grumpy=[0, 1, 0, 1, 0, 1, 0, 1],
        minutes=2))

    print(Solution().maxSatisfied(
        customers=[1],
        grumpy=[0],
        minutes=1)
    )


if __name__ == '__main__':
    test()
