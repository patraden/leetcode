from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node = head
        prev = root = None
        prefix = 0

        while node:
            prefix += node.val
            if node.val == 0 and prefix > 0:
                n = ListNode(prefix)
                prefix = 0
                if not prev:
                    prev = n
                    root = n
                else:
                    prev.next = n
                    prev = n
            node = node.next
        return root



def generate(vals):
    prev = head = None
    for val in vals:
        node = ListNode(val)
        if not head:
            head = node
        if prev:
            prev.next = node
        prev = node
    return head


def test():
    print(Solution().mergeNodes(head=generate([0, 3, 1, 0, 4, 5, 2, 0])))


if __name__ == '__main__':
    test()
