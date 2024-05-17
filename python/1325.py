from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def helper(node, parent=None, direction=None):
            if node is None:
                return

            helper(node.left, node, 0)
            helper(node.right, node, 1)

            if node.val == target and node.left is None and node.right is None:
                if parent is not None:
                    if direction == 0:
                        parent.left = None
                    elif direction == 1:
                        parent.right = None
                else:
                    return None
            return node

        return helper(root)


def list_to_tree(a: list):
    n = len(a)
    for i in range(n - 1, 1, -1):
        if a[i] is not None and not isinstance(a[i], TreeNode):
            a[i] = TreeNode(a[i])

        parent = i // 2
        if not isinstance(a[parent], TreeNode):
            a[parent] = TreeNode(a[parent])

        if i % 2 == 0:
            a[parent].left = a[i]
        else:
            a[parent].right = a[i]


def walk_tree(root: Optional[TreeNode]):
    """ pre-order traversal """
    if root is not None:
        print(root.val)
        walk_tree(root.left)
        walk_tree(root.right)


def test():
    head = [None, 1, 2, 3, 2, None, 2, 4]
    # head = [1, 3, 3, 3, 2]
    head = [None] + head
    list_to_tree(a=head)
    root = head[1]
    walk_tree(root)


if __name__ == '__main__':
    test()
