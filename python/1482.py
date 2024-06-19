from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        days = sorted(set(bloomDay))
        lo, hi = 0, len(days)

        while lo < hi:
            mi = (lo + hi) // 2
            res = count = 0
            for day in bloomDay:
                if day > days[mi]:
                    count = 0
                else:
                    count += 1

                if count == k:
                    res += 1
                    count = 0

                if res == m:
                    break

            if res < m:
                lo = mi + 1
            else:
                hi = mi

        if hi == len(days):
            return -1

        return days[hi]


def test():
    print(Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))
    print(Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2))
    print(Solution().minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3))


if __name__ == '__main__':
    test()
