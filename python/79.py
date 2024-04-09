from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        alphabet = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                alphabet.add(board[r][c])

        for c in set(word):
            if c not in alphabet:
                return False

        def backtrack(i, j, w: str, p: set):
            nonlocal board
            if board[i][j] == w:
                return True

            if board[i][j] == w[0]:
                w = w[1:]
                for k, m in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= k < len(board) and 0 <= m < len(board[0]) and (k, m) not in path:
                        p.add((i, j))
                        if backtrack(k, m, w, p):
                            return True
                        p.remove((i, j))

        for r in range(len(board)):
            for c in range(len(board[0])):
                path = set()
                if backtrack(r, c, word, path):
                    return True
        return False


def test():
    print(Solution().exist(
        board=[["A", "B", "C", "E"],
               ["S", "F", "C", "S"],
               ["A", "D", "E", "E"]],
        word="ABCCED"
    ))

    print(Solution().exist(
        board=[["A", "B", "C", "E"],
               ["S", "F", "C", "S"],
               ["A", "D", "E", "E"]],
        word="SEE"
    ))

    print(Solution().exist(
        board=[["A", "B", "C", "E"],
               ["S", "F", "C", "S"],
               ["A", "D", "E", "E"]],
        word="ABCB"
    ))

    print(Solution().exist(
        board=[
            ["A", "B", "C", "E"],
            ["S", "F", "E", "S"],
            ["A", "D", "E", "E"]
        ],
        word="ABCESEEEFS"
    ))

    print(Solution().exist(
        board=[
            ["A", "B", "C", "E"],
        ],
        word="ECB"
    ))


if __name__ == '__main__':
    test()
