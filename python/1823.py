class Solution:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

    def findTheWinner(self, n: int, k: int) -> int:
        prev = node = root = None
        for i in range(n):
            node = self.Node(i + 1)
            if not root:
                root = node

            node.prev = prev

            if prev:
                prev.next = node
            prev = node

        if node:
            node.next = root
            root.prev = node

        count = 0
        node = root
        while node.next != node:
            count += 1
            if count == k:
                node.prev.next = node.next
                node.next.prev = node.prev
                count = 0
            node = node.next

        return node.val


def test():
    print(Solution().findTheWinner(n=5, k=2))
    print(Solution().findTheWinner(n=6, k=5))
    print(Solution().findTheWinner(n=2, k=1))


if __name__ == '__main__':
    test()
