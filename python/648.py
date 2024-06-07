from typing import List


class Node:
    def __init__(self):
        self.symbols = {}
        self.terminal = False


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        root = Node()
        for word in dictionary:
            node = root
            for c in word:
                node = node.symbols.setdefault(c, Node())
            node.terminal = True

        res = []
        for word in sentence.split():
            term = -1
            node = root
            for i, c in enumerate(word):
                if c not in node.symbols:
                    break
                if c in node.symbols:
                    node = node.symbols[c]
                    if node.terminal:
                        term = i
                        break
            res.append(word[:term + 1] if term != -1 else word)

        return " ".join(res)


def test():
    # print(Solution().replaceWords(
    #     dictionary=["cat", "bat", "rat"],
    #     sentence="the cattle was rattled by the battery"
    # ))
    # print(Solution().replaceWords(
    #     dictionary=["a", "b", "c"],
    #     sentence="aadsfasf absbs bbab cadsfafs"
    # ))
    print(Solution().replaceWords(
        dictionary=["a", "aa", "aaa", "aaaa"],
        sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    ))


if __name__ == '__main__':
    test()
