from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = pprev = None
        node = head

        i = 0
        f = p = -1

        mn = float('inf')
        mx = float('-inf')

        while node:
            if prev and pprev:
                if ((prev.val > node.val and prev.val > pprev.val) or
                        (prev.val < node.val and prev.val < pprev.val)):
                    if p != -1:
                        mn = min(mn, i - p)
                    if f != -1:
                        mx = max(mx, i - f)

                    p = i
                    if f == -1:
                        f = p

            pprev = prev
            prev = node
            node = node.next
            i += 1

        return [mn if mn != float('inf') else -1, mx if mx != float('-inf') else -1]


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
    print(Solution().nodesBetweenCriticalPoints(head=None))
    print(Solution().nodesBetweenCriticalPoints(head=generate([3, 1])))
    print(Solution().nodesBetweenCriticalPoints(head=generate([5, 3, 1, 2, 5, 1, 2])))
    print(Solution().nodesBetweenCriticalPoints(head=generate([1, 3, 2, 2, 3, 2, 2, 2, 7])))


if __name__ == '__main__':
    test()
