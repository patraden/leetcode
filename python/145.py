from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        current = root
        res = []
        while True:
            while current:
                stack.append((current, False))
                current = current.left
            if stack:
                node, traversed = stack.pop()
                if traversed:
                    res.append(node.val)
                    continue
                stack.append((node, True))
                current = node.right
            else:
                break
        return res


def main():
    n4 = TreeNode(val=4)
    n3 = TreeNode(val=3)
    n2 = TreeNode(val=2, left=n3, right=n4)
    n1 = TreeNode(val=1, right=n2)
    print(Solution().postorderTraversal(n1))
    print(Solution().postorderTraversal(n2))


if __name__ == "__main__":
    main()
