from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if node is None:
                return 0
            d = helper(node.next)
            res = (node.val * 2) // 10
            node.val = (node.val * 2) % 10 + d
            return res

        digit = helper(head)
        if digit == 0:
            return head
        root = ListNode(digit, head)
        return root


def test():
    root = generate_list(head = [1,8,9])
    new_root = Solution().doubleIt(root)
    walk_list(new_root)


if __name__ == '__main__':
    test()
