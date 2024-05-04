from typing import List, Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []

        node = head
        m = 0
        while node and m < k:
            stack.append(node)
            node = node.next
            m += 1

        if len(stack) < k:
            return head

        root = prev = stack.pop()
        nxt = prev.next
        while stack:
            node = stack.pop()
            prev.next = node
            prev = node

        prev.next = self.reverseKGroup(nxt, k)
        return root


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


def walk_list(root):
    node = root
    while node:
        print(node.val)
        node = node.next


def test():
    head = [5]
    root = generate_list(head=head)
    walk_list(root)
    print("=" * 10)
    new_root = Solution().reverseKGroup(root, k=1)
    walk_list(new_root)


if __name__ == '__main__':
    test()
