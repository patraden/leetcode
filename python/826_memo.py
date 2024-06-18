from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        mxa = max(worker)
        dp = [0] * (mxa + 1)

        n = len(difficulty)
        for i in range(n):
            if difficulty[i] <= mxa:
                dp[difficulty[i]] = max(profit[i], dp[difficulty[i]])

        for i in range(1, mxa + 1):
            dp[i] = max(dp[i], dp[i - 1])

        res = 0
        for w in worker:
            res += dp[w]

        return res


def test():
    print(Solution().maxProfitAssignment(
        difficulty=[2, 4, 6, 8, 10],
        profit=[10, 20, 30, 40, 50],
        worker=[4, 5, 6, 7]))

    print(Solution().maxProfitAssignment(
        difficulty=[68, 35, 52, 47, 86],
        profit=[67, 17, 1, 81, 3],
        worker=[92, 10, 85, 84, 82]))


if __name__ == '__main__':
    test()
