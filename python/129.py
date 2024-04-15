from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [(root, "")]
        res = 0
        while stack:
            n, prefix = stack.pop()
            prefix += str(n.val)
            if n.left is None and n.right is None:
                res += int(prefix)
            if n.left:
                stack.append((n.left, prefix))
            if n.right:
                stack.append((n.right, prefix))

        return res



def test():
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n0 = TreeNode(0)
    n9 = TreeNode(9, n5, n1)
    root = TreeNode(4, n9, n0)
    print(Solution().sumNumbers(root))
    print(Solution().sumNumbers(n9))


if __name__ == '__main__':
    test()
