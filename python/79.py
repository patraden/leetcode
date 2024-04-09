from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        alphabet = {}
        for r in range(len(board)):
            for c in range(len(board[0])):
                alphabet[board[r][c]] = alphabet.get(board[r][c], 0) + 1

        word_d = {}
        for c in word:
            word_d[c] = word_d.get(c, 0) + 1

        for c, v in word_d.items():
            if c not in alphabet or alphabet[c] < v:
                return False

        def backtrack(i, j, p):
            if board[i][j] == word[p]:
                if p == len(word) - 1:
                    return True

                for k, m in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= k < len(board) and 0 <= m < len(board[0]):
                        temp = board[i][j]
                        board[i][j] = ''
                        if backtrack(k, m, p + 1):
                            return True
                        board[i][j] = temp

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
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
        word="ABCESEFE"
    ))

    print(Solution().exist(
        board=[
            ["A", "B", "C", "E"],
        ],
        word="ECB"
    ))


if __name__ == '__main__':
    test()
