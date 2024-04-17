from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def from_list(self, vals: List[int]):
        if len(vals) == 0:
            return

        nodes = [None] * (len(vals) + 1)
        for i in range(1, len(vals) + 1):
            parent_idx = i // 2
            parent = nodes[parent_idx]
            if vals[i - 1] is not None:
                nodes[i] = TreeNode(vals[i - 1])
            if parent:
                if i % 2 == 0:
                    parent.left = nodes[i]
                else:
                    parent.right = nodes[i]
        return nodes[1]


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        stack = [(root, [root.val])]
        mn_prefix = None
        while stack:
            node, prefix = stack.pop()
            if node.left is None and node.right is None:
                mn_prefix = prefix[::-1] if mn_prefix is None else min(prefix[::-1], mn_prefix)
            if node.left is not None:
                stack.append((node.left, prefix + [node.left.val]))
            if node.right is not None:
                stack.append((node.right, prefix + [node.right.val]))
        return "".join(chr(97 + num) for num in mn_prefix)


def test():
    root = TreeNode().from_list([2,2,1,None,1,0,None, None, None,0])
    layer = [root]
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

    print(Solution().smallestFromLeaf(root))


if __name__ == '__main__':
    test()
