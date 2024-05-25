from typing import List


class Node:
    def __init__(self):
        self.symbols = {}
        self.terminal = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(i=0, prefix=None):
            nonlocal trie, res

            if i == len(s):
                res.append(" ".join(prefix))
                return

            prefix = prefix or []
            n = trie
            for j in range(i, len(s) + 1):
                if n.terminal:
                    prefix.append(s[i:j])
                    helper(j, prefix)
                    prefix.pop()

                if j == len(s) or s[j] not in n.symbols:
                    return

                n = n.symbols[s[j]]

        trie = Node()
        res = []
        for word in wordDict:
            node = trie
            for letter in word:
                node = node.symbols.setdefault(letter, Node())
            node.terminal = True

        helper(0)
        return res


def test():
    print(Solution().wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
    print(Solution().wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"]))
    print(Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))


if __name__ == '__main__':
    test()
