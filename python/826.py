from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pd = []
        mp = 0
        for d, p in sorted(zip(difficulty, profit)):
            mp = max(mp, p)
            pd.append((d, mp))

        res = 0
        for w in worker:
            lo, hi = 0, len(pd)
            while lo < hi:
                mi = (lo + hi) // 2
                if pd[mi][0] > w:
                    hi = mi
                else:
                    lo = mi + 1

            res += pd[lo - 1][1] if lo > 0 else 0

        return res


def test():
    print(Solution().maxProfitAssignment(
        difficulty=[2, 4, 6, 8, 10],
        profit=[10, 20, 30, 40, 50],
        worker=[4, 5, 6, 7]))

    print(Solution().maxProfitAssignment(
        difficulty=[85, 40, 40],
        profit=[24, 66, 99],
        worker=[40, 25, 40]))

    print(Solution().maxProfitAssignment(
        difficulty=[8],
        profit=[10],
        worker=[4, 5, 6, 7]))

    print(Solution().maxProfitAssignment(
        difficulty=[68, 35, 52, 47, 86],
        profit=[67, 17, 1, 81, 3],
        worker=[92, 10, 85, 84, 82]))


if __name__ == '__main__':
    test()
