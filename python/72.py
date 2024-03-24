from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        if n > m:
            word1, word2 = word2, word1
            n, m = m, n

        curr = list(range(n + 1))
        for i in range(1, m + 1):
            prev, curr = curr, [i] + [0] * n
            for j in range(1, n + 1):
                curr[j] = min(
                    prev[j] + 1,
                    curr[j - 1] + 1,
                    prev[j - 1] + int(word1[j - 1] != word2[i - 1])
                )
        return curr[n]


def test():
    # print(Solution().minDistance(word1="intention", word2="execution"))
    # print(Solution().minDistance(word1="horse", word2="ros"))
    print(Solution().minDistance(word1="", word2="ate"))


if __name__ == '__main__':
    test()
