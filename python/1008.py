from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(start: int, end: int) -> Optional[TreeNode]:
            if start < n and start < end:
                node = TreeNode(preorder[start])
                r = right[start]
                node.left = helper(start + 1, r)
                node.right = helper(r, end)
                return node

        n = len(preorder)
        stack = []
        right = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and preorder[stack[-1]] < preorder[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        return helper(0, n)


def main():
    sol = Solution()
    root = sol.bstFromPreorder(preorder=[8, 5, 1, 7, 10, 12])


if __name__ == "__main__":
    main()
