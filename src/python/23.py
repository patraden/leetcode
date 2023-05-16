# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next





def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    from queue import PriorityQueue
    n = len(lists)
    q = PriorityQueue(n)
    for i in range(n):
        if lists[i]:
            q.put((lists[i].val, i))
            lists[i] = lists[i].next

    if q.qsize() > 0:
        node = None
        first = None
        while q.qsize() > 0:
            val, k = q.get()
            if node is not None:
                node.next = ListNode(val)
                node = node.next
            else:
                node = ListNode(val)
                first = node
            if lists[k]:
                q.put((lists[k].val, k))
                lists[k] = lists[k].next
        return first


def main():
    def linked_list(a: list) -> ListNode:
        if len(a) > 0:
            node = ListNode(val=a[-1])
            for i in range(len(a) - 2, -1, -1):
                node = ListNode(val=a[i], next=node)
            return node

    node = mergeKLists([linked_list([50, 51, 78]), linked_list([1, 3, 4]), linked_list([2, 6])])
    # node = mergeKLists([linked_list([1, 55]), linked_list([1]), linked_list([1, 65])])
    # node = mergeKLists([linked_list([]), linked_list([]), linked_list([])])
    while node:
        print(node.val)
        node = node.next


if __name__ == "__main__":
    main()
