def binary_search(a: list, target: int):
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] == target:
            return m
        elif target < a[m]:
            r = m
        else:
            l = m + 1
    return -1


def another_binary_search(a: list, target: int):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == target:
            return m
        elif target < a[m]:
            r = m
        else:
            l = m + 1
    return -1


def another_binary_search_right_most(a: list, target: int):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if target == a[m]:
            return True
        elif target < a[m]:
            r = m - 1
        else:
            l = m + 1
    return r + 1


def tests():
    assert binary_search([1], 1) == 0
    assert binary_search([1, 2, 3, 4], 2) == 1
    assert binary_search([1, 2, 3, 4], 4) == 3
    assert binary_search([], 1) == -1

    assert another_binary_search([1], 1) == 0
    assert another_binary_search([1, 2, 3, 4], 2) == 1
    assert another_binary_search([1, 2, 3, 4], 4) == 3
    assert another_binary_search([], 1) == -1

    print(another_binary_search_right_most([8, 9], 7))


if __name__ == '__main__':
    tests()
