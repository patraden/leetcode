def binary_search_in_sorted_matrix(
        mat: list[list[int]],
        target: int,
        col_l: int,
        col_r: int,
        row_u: int,
        row_d: int
) -> bool:
    if col_l == col_r or row_u == row_d:
        def _list(i): return mat[i][col_l] if col_l == col_r else mat[row_u][i]
        l, r = (row_u, row_d + 1) if col_l == col_r else (col_l, col_r + 1)
        while l < r:
            m = (l + r) // 2
            if _list(m) == target:
                return True
            elif target < _list(m):
                r = m
            else:
                l = m + 1
        return False
    else:
        n, m = row_d - row_u, col_r - col_l
        n, m = (m, n) if m < n else (n, m)


def tests():
    m1 = [[1], [2], [5], [5], [10], [55]]
    m2 = [[1, 2, 5, 5, 10, 55]]

    assert not binary_search_in_sorted_matrix(m1, 0, col_l=0, col_r=0, row_u=0, row_d=len(m1))
    assert binary_search_in_sorted_matrix(m1, 2, col_l=0, col_r=0, row_u=0, row_d=len(m1))
    assert binary_search_in_sorted_matrix(m1, 55, col_l=0, col_r=0, row_u=0, row_d=len(m1))

    assert not binary_search_in_sorted_matrix(m2, 0, col_l=0, col_r=len(m2[0]), row_u=0, row_d=0)
    assert binary_search_in_sorted_matrix(m2, 2, col_l=0, col_r=len(m2[0]), row_u=0, row_d=0)
    assert binary_search_in_sorted_matrix(m2, 55, col_l=0, col_r=len(m2[0]), row_u=0, row_d=0)


if __name__ == "__main__":
    tests()
