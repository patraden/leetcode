from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None:
            return head

        node = head
        size = 1
        while node.next:
            node = node.next
            size += 1
        last = node

        k %= size

        if k == 0 or size == 1:
            return head

        i = 1
        node = head
        while i < size - k:
            node = node.next
            i += 1

        root = node.next
        node.next = None
        last.next = head

        return root


def test():
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

    # head = [1, 2]
    head = [1, 2, 3, 4, 5]
    node = Solution().rotateRight(generate_list(head), 20)

    while node:
        print(node.val)
        node = node.next


if __name__ == '__main__':
    test()
