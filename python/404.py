from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        from_right = True
        current = root
        stack = []
        while True:
            if current is not None:
                stack.append(current)
                if current.left is None and current.right is None and not from_right:
                    res += current.val
                current = current.left
                from_right = False
                continue
            elif stack:
                current = stack.pop()
                current = current.right
                from_right = True
            else:
                break
        return res

def test():
    tn15 = TreeNode(15)
    tn7 = TreeNode(7)
    tn9 = TreeNode(9)
    tn20 = TreeNode(20, tn15, tn7)
    root = TreeNode(3, tn9, tn20)
    print(Solution().sumOfLeftLeaves(root))
    print(Solution().sumOfLeftLeaves(tn9))


if __name__ == '__main__':
    test()
