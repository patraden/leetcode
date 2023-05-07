from collections import namedtuple

Cell = namedtuple('Cell', ['row', 'col'])


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
    :return: True if target exists else False
    """
    n, m = len(mat), len(mat[0]) if len(mat) > 0 else 0

    if (n == 0 or
            top.row >= bot.row or
            top.col >= bot.col or
            top.row >= n or
            top.col >= m or
            bot.row <= 0 or
            bot.col <= 0):
        return False

    left = top
    if top.row + 1 == bot.row:
        one = Cell(0, 1)
        right = Cell(top.row, bot.col)
        def less(x, y): return x.col < y.col
    elif top.col + 1 == bot.col:
        one = Cell(1, 0)
        right = Cell(bot.row, top.col)
        def less(x, y): return x.row < y.row
    else:
        one = Cell(1, 1)
        sqr_size = min(bot.row - top.row, bot.col - top.col)
        right = Cell(top.row + sqr_size, top.col + sqr_size)
        def less(x, y): return x.row < y.row and x.col < y.col

    while less(left, right):
        mid = Cell(
            (left.row + right.row) // 2,
            (left.col + right.col) // 2
        )
        if mat[mid.row][mid.col] == target:
            return True
        elif target < mat[mid.row][mid.col]:
            right = mid
        else:
            left = Cell(mid.row + one.row, mid.col + one.col)

    if one != Cell(1, 1):
        return False

    return (
            matrix_binary_search(mat, target, Cell(top.row, right.col), Cell(right.row, bot.col)) or
            matrix_binary_search(mat, target, Cell(right.row, top.col), Cell(bot.row, right.col))
    )


def main():
    with open('input.txt', mode='r') as f:
        target = int(f.readline().rstrip())
        n = int(f.readline().rstrip())
        m = int(f.readline().rstrip())
        mat = [[int(num) for num in f.readline().rstrip().split()] for _ in range(n)]

    print(matrix_binary_search(mat, target, Cell(0, 0), Cell(n, m)))


if __name__ == "__main__":
    main()
