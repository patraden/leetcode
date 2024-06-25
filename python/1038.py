from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        prefix = 0
        stack = [root]
        current = root
        while True:
            if current:
                current = current.right
                if current:
                    stack.append(current)
            elif stack:
                current = stack.pop()
                prefix += current.val
                current.val = prefix
                current = current.left
                if current:
                    stack.append(current)
            else:
                break
        return root

    def bstToGstRec(self, root: TreeNode) -> TreeNode:
        prefix = 0

        def helper(node):
            nonlocal prefix
            if not node:
                return
            helper(node.right)
            prefix += node.val
            node.val = prefix
            helper(node.left)

        helper(root)
        return root


def test():
    pass


if __name__ == '__main__':
    test()
