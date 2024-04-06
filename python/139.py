from typing import List


class Solution:
    class Node:
        def __init__(self):
            self.terminal = False
            self.symbols = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = self.Node()
        for word in wordDict:
            node = root
            for char in word:
                node.symbols[char] = node.symbols.get(char, self.Node())
                node = node.symbols[char]
            node.terminal = True

        m = len(s)
        dp = [True] + [False] * m

        for i in range(m):
            if dp[i]:
                j = i
                node = root
                while j < m and s[j] in node.symbols:
                    node = node.symbols[s[j]]
                    j += 1
                    if node.terminal:
                        dp[j] = True
                        if j == m:
                            return True
        return dp[-1]


def test():
    print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))
    print(Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))


if __name__ == '__main__':
    test()
