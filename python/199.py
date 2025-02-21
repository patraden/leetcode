from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def helper(level: list):
            nonlocal res

            if len(level) == 0:
                return

            res.append(level[-1].val)
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            helper(next_level)

        res = []
        if not root:
            return res

        helper([root])

        return res


def test():
    s = Solution()
    s.rightSideView(None)


if __name__ == '__main__':
    test()
