from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(a):
            if len(a) == 0:
                return None

            if len(a) == 1:
                return TreeNode(a[0])

            m = len(a) // 2
            root = TreeNode(a[m])
            root.left = helper(a[:m])
            root.right = helper(a[m+1:])
            return root

        return helper(nums)









def test():
    pass


if __name__ == '__main__':
    test()
