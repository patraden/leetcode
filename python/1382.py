# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            nonlocal nums
            if node:
                inorder(node.left)
                nums.append(node.val)
                inorder(node.right)

        def balanced(a):
            if a:
                m = len(a) // 2
                node = TreeNode(a[m])
                node.left = balanced(a[:m])
                node.right = balanced(a[m + 1:])
                return node

        nums = []
        inorder(root)
        return balanced(nums)


def test():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    new_root = Solution().balanceBST(root)
    print(new_root.val)


if __name__ == '__main__':
    test()
