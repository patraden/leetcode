from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node is None:
                return 0, 0

            l_debt, l_count = helper(node.left)
            r_debt, r_count = helper(node.right)
            debt = node.val - 1 + l_debt + r_debt
            count = l_count + r_count + abs(debt)
            return debt, count

        debt, count = helper(root)
        assert debt == 0
        return count


def test():
    root = TreeNode(0)
    root.left = TreeNode(6)
    root.right = TreeNode(1)
    root.right.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(0)
    root.left.right.left = TreeNode(0)
    root.left.right.right = TreeNode(0)

    print(Solution().distributeCoins(root))


if __name__ == '__main__':
    test()
