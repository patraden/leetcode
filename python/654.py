from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        nodes = [None] * n
        stack = []
        left = [-1] * n
        mx = 0
        for i in range(n):
            #  aux actions for find max value index and map nums to nodes
            if nums[i] > nums[mx]:
                mx = i
            nodes[i] = TreeNode(val=nums[i])
            #  end of aux actions

            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        right = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            l, r = left[i], right[i]
            if l > -1 and r < n:
                if nums[l] < nums[r]:
                    nodes[l].right = nodes[i]
                else:
                    nodes[r].left = nodes[i]
            elif l > -1:
                nodes[l].right = nodes[i]
            elif r < n:
                nodes[r].left = nodes[i]

        return nodes[mx]


def main():
    node1 = Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    node2 = Solution().constructMaximumBinaryTree([3, 2, 1])
    node3 = Solution().constructMaximumBinaryTree([10])


if __name__ == "__main__":
    main()
