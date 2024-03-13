from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solution_helper(node):
            val = node.val

            if node.left is None and node.right is None:
                return node.val, node.val
            elif node.left is None and node.right is not None:
                max_inside_right, max_up_to_rt_right = solution_helper(node.right)
                max_up_to_rt = max(val, val + max_up_to_rt_right)
                max_inside = max(max_up_to_rt, max_inside_right)
                return max_inside, max_up_to_rt
            elif node.left is not None and node.right is None:
                max_inside_left, max_up_to_rt_left = solution_helper(node.left)
                max_up_to_rt = max(val, val + max_up_to_rt_left)
                max_inside = max(max_up_to_rt, max_inside_left)
                return max_inside, max_up_to_rt

            max_inside_left, max_up_to_rt_left = solution_helper(node.left)
            max_inside_right, max_up_to_rt_right = solution_helper(node.right)
            max_up_to_rt = max(val, val + max(max_up_to_rt_left, max_up_to_rt_right))
            max_inside = max(
                max_up_to_rt,
                val + max_up_to_rt_left + max_up_to_rt_right,
                max_inside_left,
                max_inside_right
            )
            return max_inside, max_up_to_rt

        return max(solution_helper(root))




def test():
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node20 = TreeNode(20, node15, node7)
    node9 = TreeNode(9)
    root = TreeNode(-10, node9, node20)
    print(Solution().maxPathSum(node20))

    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(Solution().maxPathSum(root))

    node_neg1 = TreeNode(-1)
    node1 = TreeNode(1, left=node_neg1)
    node3 = TreeNode(3)
    node_neg2 = TreeNode(-2, node1, node3)
    node_neg3 = TreeNode(-3, TreeNode(-2))
    root = TreeNode(1, node_neg2, node_neg3)
    print(Solution().maxPathSum(root))


if __name__ == '__main__':
    test()
