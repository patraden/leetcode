from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        a = []
        while node:
            a.append(node.val)
            node = node.next
        assert len(a) % 2 == 0

        s = -float('inf')
        for i in range(len(a) // 2 + 1):
            s = max(s, a[i] + a[len(a) - 1 - i])
        return s


def main():
    def linkenize(a: list):
        if len(a) > 0:
            prev = None
            for i in range(len(a) - 1, -1, -1):
                n = ListNode(a[i], prev)
                prev = n
            return n

    s = Solution()
    # head = linkenize([4, 2, 2, 3])
    head = linkenize([5, 4, 2, 1])
    # head = linkenize([1, 100000])
    node = head
    s.pairSum(head)


if __name__ == "__main__":
    main()
