from typing import List


def get_line_hash(p1: tuple, p2: tuple) -> tuple:
    p1x, p1y = p1
    p2x, p2y = p2
    if p1x == p2x:
        return p1x, "inf"
    if p1y == p2y:
        return "inf", p2y

    a = (p2y - p1y) / (p2x - p1x)
    b = (p1x * p2y - p2x * p1y) / (p1x - p2x)
    return a, b


class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        d = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = tuple(points[i]), tuple(points[j])
                h = get_line_hash(p1, p2)
                if h not in d:
                    d[h] = set()
                d[h].add(p1)
                d[h].add(p2)

        res = 0
        for h in d:
            res = max(res, len(d[h]))
        return res


def main():
    print(Solution().maxPoints(points=[[0, 0]]))
    print(Solution().maxPoints(points=[[1, 1], [2, 2], [3, 3]]))
    print(Solution().maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
    print(Solution().maxPoints(points=[[0, 100], [1, 100], [5, 3], [4, 1], [4, 100], [10, 100]]))


if __name__ == "__main__":
    main()
