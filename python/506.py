from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        res = [None] * len(score)

        for i, (j, score) in enumerate(s):
            if i == 0:
                e = "Gold Medal"
            elif i == 1:
                e = "Silver Medal"
            elif i == 2:
                e = "Bronze Medal"
            else:
                e = str(i + 1)
            res[j] = e
        return res


def test():
    print(Solution().findRelativeRanks(score=[10, 3, 8, 9, 4]))
    print(Solution().findRelativeRanks(score=[5, 4, 3, 2, 1]))


if __name__ == '__main__':
    test()
