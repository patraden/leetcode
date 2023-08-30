from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        current = root
        res = []
        while True:
            while current:
                stack.append(current)
                current = current.left
            if stack:
                current = stack.pop()
                res.append(current.val)
                current = current.right
            else:
                break
        return res


def main():
    n4 = TreeNode(val=4)
    n3 = TreeNode(val=3)
    n2 = TreeNode(val=2, left=n3, right=n4)
    n1 = TreeNode(val=1, right=n2)
    print(Solution().inorderTraversal(n1))
    print(Solution().inorderTraversal(n2))


if __name__ == "__main__":
    main()
