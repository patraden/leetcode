from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hash = dict(zip(inorder, range(len(inorder))))

        def helper(idx, start, end) -> Optional[TreeNode]:
            nonlocal preorder, inorder_hash
            # print("===>", preorder[idx], start, end)

            if not (0 <= idx < len(preorder)):
                return None

            m = inorder_hash[preorder[idx]]
            if start >= end or not (start <= m < end):
                return None

            root = TreeNode(preorder[idx])
            root.left = helper(idx + 1, start, m)
            root.right = helper(idx + m - start + 1, m + 1, end)

            return root

        return helper(0, 0, len(preorder))

    def preorder(self, root: Optional[TreeNode]):
        if root is None:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)


def test():
    s = Solution()
    # root = s.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
    root = s.buildTree(preorder=[3, 9, 43, 45, 42, 46, 44, 20, 15, 7], inorder=[42, 45, 46, 43, 44, 9, 3, 15, 20, 7])
    # root = s.buildTree(preorder=[20, 15, 7], inorder=[15, 20, 7])
    s.preorder(root)
    print("=" * 10)
    s.inorder(root)


if __name__ == '__main__':
    test()
