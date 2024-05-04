from typing import List, Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        node = head
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            if not nxt:
                return node
            node = nxt


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        count = 0
        prev = None
        node = head
        while node and count < k:
            nxt = node.next
            node.next = prev
            prev = node
            count += 1
            node = nxt





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
    root = generate_list(head=[1, 22, 3, 4, 5])
    walk_list(root)
    # walk_list(root)
    print("=" * 10)
    new_root = Solution().reverse(root)
    walk_list(new_root)


if __name__ == '__main__':
    test()
