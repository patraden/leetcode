from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q)

    def helper(self, root, p, q):
        if root is None:
            return

        if root == p or root == q:
            return root

        l = self.helper(root.left, p, q)
        r = self.helper(root.right, p, q)

        if l is None and r is None:
            return
        elif l is None:
            return r
        elif r is None:
            return l

        return root


def test():
    pass


if __name__ == '__main__':
    test()
