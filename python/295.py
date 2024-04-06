import heapq


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right) == 0:
            self.left.append(-num)
            return

        left = - self.left[0]

        # should go to left
        if num <= left and len(self.left) <= len(self.right):
            heapq.heappush(self.left, -num)
            return

        # should go to left but balanced
        if num <= left and len(self.left) > len(self.right):
            heapq.heappush(self.left, -num)
            top = - heapq.heappop(self.left)
            heapq.heappush(self.right, top)
            return

        # should go to right
        if num > left and len(self.left) >= len(self.right):
            heapq.heappush(self.right, num)
            return

        # should go to right but balanced
        if num > left and len(self.left) < len(self.right):
            heapq.heappush(self.right, num)
            top = heapq.heappop(self.right)
            heapq.heappush(self.left, -top)
            return

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        if len(self.left) < len(self.right):
            return self.right[0]
        return (self.right[0] - self.left[0]) / 2


def test_case1():
    # 1, 2, 3
    return [
        ("MedianFinder", 0),
        ("addNum", 1),
        ("addNum", 2),
        ("findMedian", 0),
        ("addNum", 3),
        ("findMedian", 0)
    ]


def test_case2():
    # -203, -22, -10, 2, 22, 44
    return [
        ("MedianFinder", 0),
        ("addNum", -10),
        ("addNum", 2),
        ("findMedian", 0),
        ("addNum", -203),
        ("addNum", -22),
        ("addNum", 22),
        ("addNum", 44),
        ("findMedian", 0)
    ]


def test_case3():
    return [
        ("MedianFinder", 0),
        ("addNum", -10),
        ("findMedian", 0),
    ]


def test(test_case: list):
    finder = None
    for method, num in test_case:
        val = None
        if method == "MedianFinder":
            finder = MedianFinder()
        elif method == "addNum":
            finder.addNum(num)
        elif method == "findMedian":
            val = finder.findMedian()
        print(val)
    print(finder.left, finder.right)


if __name__ == '__main__':
    test(test_case2())
