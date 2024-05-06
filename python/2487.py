from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while node:
            while stack and stack[-1].val < node.val:
                stack.pop()
            stack.append(node)
            node = node.next

        root = None
        for i in range(len(stack)):
            node = stack[i]
            if not root:
                root = node
            node.next = stack[i + 1] if i + 1 < len(stack) else None

        return root


def walk_list(root):
    node = root
    while node:
        print(node.val)
        node = node.next


def generate_list(head: list):
    prev = root = None
    for num in head:
        node = ListNode(val=num)
        if prev:
            prev.next = node
        else:
            root = node
        prev = node
    return root


def test():
    # root = generate_list([5, 2, 13, 3, 8])
    root = generate_list(head=[1, 1, 1, 1])
    walk_list(root)
    new_root = Solution().removeNodes(root)
    print("=" * 30)
    walk_list(new_root)


if __name__ == '__main__':
    test()
