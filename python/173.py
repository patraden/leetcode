from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
        current = self.root
        while current:
            self.stack.append(current)
            current = current.left

    def next(self) -> int:
        if self.stack:
            node = self.stack.pop()
            val = node.val
            current = node.right
            while current:
                self.stack.append(current)
                current = current.left
            return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


def main():
    node9 = TreeNode(val=9)
    node20 = TreeNode(val=20)
    node15 = TreeNode(val=15, left=node9, right=node20)
    node3 = TreeNode(val=3)
    node7 = TreeNode(val=7, left=node3, right=node15)
    iter = BSTIterator(node7)

    print(iter.hasNext(), iter.next())
    print(iter.hasNext(), iter.next())
    print(iter.hasNext(), iter.next())
    print(iter.hasNext(), iter.next())
    print(iter.hasNext(), iter.next())
    print(iter.hasNext(), iter.next())


if __name__ == "__main__":
    main()
