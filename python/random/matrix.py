"""
Given a square matrix of 0s and 1s,
you need to "zero" all "islands" made of 1s
which are not connected to the matrix border.
"""


def test_case():
    return [
        [1, 0, 0, 1, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ], [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]


def main():
    mtx, mtx_expected = test_case()
    n = len(mtx)

    def matrix_dfs(i, j):
        mtx[i][j] = 0
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= x < n and 0 <= y < n and mtx[x][y] == 1:
                matrix_dfs(x, y)

    for k in range(n):
        for x, y in ((0, k), (n - 1, k), (k, 0), (k, n - 1)):  # iterating throw matrix border elements
            if mtx[x][y] == 1:
                matrix_dfs(x, y)

    assert mtx == mtx_expected


if __name__ == "__main__":
    main()
