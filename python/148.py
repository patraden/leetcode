from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortHelper(self, start, size):
        if size == 1:
            return start

        mid = start
        count = 1
        while count < size // 2:
            mid = mid.next
            count += 1

        start_left = start
        start_right = mid.next
        mid.next = None  # disconnecting left and right lists

        left = self.sortHelper(start_left, count)
        right = self.sortHelper(start_right, size - count)

        root = prev = None

        while left or right:
            if left and right:
                if left.val <= right.val:
                    node = left
                    left = left.next
                else:
                    node = right
                    right = right.next
            elif left:
                node = left
                left = left.next
            else:
                node = right
                right = right.next

            if not prev:
                root = node
            else:
                prev.next = node
            prev = node

        return root

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        return self.sortHelper(head, size)


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

    # head = [10, 66, 2]
    # head = [-1, 5, 3, 4, 0]
    head = [4, -11, 1, 11, 9, 2, -44]
    # head = [-1]
    # head = []
    print(head)

    root = generate_list(head)
    # node = generate_list(head)
    node = Solution().sortList(root)

    while node:
        print(node.val)
        node = node.next


if __name__ == '__main__':
    test()
