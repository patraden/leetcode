from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodes = [[] for _ in range(numCourses)]
        for v, w in prerequisites:
            nodes[w].append(v)

        order = []
        white, grey, black = 0, 1, 2
        colors = [white] * numCourses

        for s in range(numCourses):
            if colors[s] == black:
                continue

            stack = [s]
            while stack:
                node = stack.pop()
                if colors[node] == white:
                    colors[node] = grey
                    stack.append(node)

                    for w in nodes[node]:
                        if colors[w] == white:
                            stack.append(w)
                        if colors[w] == grey:
                            return []

                elif colors[node] == grey:
                    colors[node] = black
                    order.append(node)

        return order[::-1]


def test():
    s = Solution()
    print(s.findOrder(numCourses=4, prerequisites=[
        [1, 0],
        [2, 0],
        [3, 1],
        [3, 2]
    ]))

    print(s.findOrder(numCourses=2, prerequisites=[[1, 0]]))
    print(s.findOrder(numCourses=1, prerequisites=[]))


if __name__ == '__main__':
    test()
