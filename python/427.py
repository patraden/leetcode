from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        def helper(tr, tc, m):
            if m == 1:
                return Node(bool(grid[tr][tc]), True, None, None, None, None)

            half = m // 2
            top_left = helper(tr, tc, half)
            top_right = helper(tr, tc + half, half)
            bot_left = helper(tr + half, tc, half)
            bot_right = helper(tr + half, tc + half, half)

            if (top_left.isLeaf and top_right.isLeaf and
                    bot_left.isLeaf and bot_right.isLeaf and
                    top_left.val == bot_left.val == top_right.val == bot_right.val):
                return Node(bool(top_left.val), True, None, None, None, None)

            return Node(False, False, top_left, top_right, bot_left, bot_right)

        return helper(0, 0, len(grid))


def test():
    root = Solution().construct(grid=[
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0]
    ])

    print(root.val, root.isLeaf)
    print("topLeft", root.topLeft.val, root.topLeft.isLeaf)
    print("topRight", root.topRight.val, root.topRight.isLeaf)
    print("bottomLeft", root.bottomLeft.val, root.bottomLeft.isLeaf)
    print("bottomRight", root.bottomRight.val, root.bottomRight.isLeaf)

    tr = root.topRight
    print(tr.topLeft.val, tr.topLeft.isLeaf)
    print(tr.topRight.val, tr.topRight.isLeaf)
    print(tr.bottomLeft.val, tr.bottomLeft.isLeaf)
    print(tr.bottomRight.val, tr.bottomRight.isLeaf)


if __name__ == '__main__':
    test()
