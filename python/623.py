from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)

        layer = [root]
        i = 1
        while layer and i < depth:
            if i == depth - 1:
                for node in layer:
                    l, r = node.left, node.right
                    node.left = TreeNode(val, left=l)
                    node.right = TreeNode(val, right=r)
                return root

            new_layer = []
            for node in layer:
                if node.left:
                    new_layer.append(node.left)
                if node.right:
                    new_layer.append(node.right)
            layer = new_layer
            i += 1


def test():
    # n1 = TreeNode(1)
    # n3 = TreeNode(3)
    # n5 = TreeNode(5)
    # n6 = TreeNode(6, left=n5)
    # n2 = TreeNode(2, left=n3, right=n1)
    # root = TreeNode(4, left=n2, right=n6)

    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n2 = TreeNode(2, left=n3, right=n1)
    root = TreeNode(4, left=n2)

    new_root = Solution().addOneRow(root, val=1, depth=3)

    layer = [new_root]
    i = 1
    while layer:
        new_layer = []
        for node in layer:
            print(i, node.val)
            if node.left:
                new_layer.append(node.left)
            if node.right:
                new_layer.append(node.right)
        layer = new_layer
        i += 1


if __name__ == '__main__':
    test()
