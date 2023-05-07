#  https://leetcode.com/problems/search-a-2d-matrix/

import functools


@functools.total_ordering
class Cell:
    def __init__(self, row: int = 1, col: int = 1):
        self.row = row
        self.col = col

    def __add__(self, other):
        return Cell(self.row + other.row, self.col + other.col)

    def __floordiv__(self, other):
        return Cell(self.row // other.row, self.col // other.col)

    def __lt__(self, other):
        return (self.row < other.row and self.col <= other.col) or \
            (self.row <= other.row and self.col < other.col)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __str__(self):
        return f"({self.row}, {self.col})"


def matrix_binary_search(
        mat: list[list[int]],
        target: int,
        top: Cell,
        bot: Cell
) -> bool:
    """
    binary search invariant is [top, bottom)
    :param mat: matrix
    :param target: searched number
    :param top: top left matrix cell
    :param bot: bottom right matrix cell + 1
    :return:
    """
    n, m = len(mat), len(mat[0]) if len(mat) > 0 else 0
    if top.row >= bot.row or top.col >= bot.col or top.row >= n or top.col >= m or bot.row <= 0 or bot.col <= 0:
        return False
    elif (top.row + 1 == bot.row) and (top.col + 1 == bot.col):
        return mat[top.row][top.col] == target
    if (top.row + 1 == bot.row) or (top.col + 1 == bot.col):
        one = Cell(0, 1) if top.row + 1 == bot.row else Cell(1, 0)
        two = Cell(2, 2)
        l = top
        r = Cell(top.row, bot.col) if top.row + 1 == bot.row else Cell(bot.row, top.col)
        while l < r:
            mid = (l + r) // two
            if mat[mid.row][mid.col] == target:
                return True
            elif target < mat[mid.row][mid.col]:
                r = mid
            else:
                l = mid + one
        return False
    else:
        sqr_size = min(bot.row - top.row, bot.col - top.col)
        sqr = Cell(sqr_size, sqr_size)
        one = Cell(1, 1)
        two = Cell(2, 2)
        l = top
        r = top + sqr
        while l < r:
            m = (l + r) // two
            if mat[m.row][m.col] == target:
                return True
            elif target < mat[m.row][m.col]:
                r = m
            else:
                l = m + one
        return matrix_binary_search(mat, target, Cell(top.row, r.col), Cell(r.row, bot.col)) or\
            matrix_binary_search(mat, target, Cell(r.row, top.col), Cell(bot.row, r.col))


def main():
    with open('input1.txt', mode='r') as f:
        target = int(f.readline().rstrip())
        n = int(f.readline().rstrip())
        m = int(f.readline().rstrip())
        mat = [[int(num) for num in f.readline().rstrip().split()] for _ in range(n)]

    print(matrix_binary_search(mat, target, Cell(0, 0), Cell(n, m)))


if __name__ == "__main__":
    main()
