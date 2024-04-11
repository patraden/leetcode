from typing import List


class Node:
    def __init__(self):
        self.symbols = {}
        self.terminal = False
        self.w = None


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        alphabet = {}
        for r in range(len(board)):
            for c in range(len(board[0])):
                alphabet[board[r][c]] = alphabet.get(board[r][c], 0) + 1

        words_filtered = []
        for word in words:
            d = {}
            add = True
            for c in word:
                d[c] = d.get(c, 0) + 1
                if c not in alphabet or d[c] > alphabet[c]:
                    add = not add
                    break
            if add:
                words_filtered.append(word)

        if not words_filtered:
            return []

        root = Node()
        for word in words_filtered:
            node = root
            for letter in word:
                node = node.symbols.setdefault(letter, Node())
            node.terminal = True
            node.w = word

        res = set()

        def backtrack(i, j, w):
            nonlocal res

            w = w.symbols[board[i][j]]
            if w.terminal:
                res.add(w.w)

            for k, m in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= k < len(board) and 0 <= m < len(board[0]) and board[k][m] in w.symbols:
                    temp = board[i][j]
                    board[i][j] = ''
                    backtrack(k, m, w)
                    board[i][j] = temp

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root.symbols:
                    backtrack(r, c, root)

        return list(res)


def test():
    print(Solution().findWords(
        board=[["o", "a", "a", "n"],
               ["e", "t", "a", "e"],
               ["i", "h", "k", "r"],
               ["i", "f", "l", "v"]],
        words=["oath", "pea", "eat", "rain"]
    ))

    print(Solution().findWords(
        board=[["a","b"],
               ["c","d"]],
        words=["abcb"]
    ))

    print(Solution().findWords(
        board=[
            ["o", "a", "b", "n"],
            ["o", "t", "a", "e"],
            ["a", "h", "k", "r"],
            ["a", "f", "l", "v"]
        ],
        words=["oa", "oaa"]
    ))

    print(Solution().findWords(
        board=[
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"]
        ],
        words=["oath", "pea", "eat", "rain", "hklf", "hf"]
    ))


if __name__ == '__main__':
    test()
