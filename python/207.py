from typing import List


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        nodes = [[] for _ in range(numCourses)]
        for v, w in prerequisites:
            nodes[v].append(w)

        white, grey, black = 0, 1, 2
        colors = [white] * numCourses

        for s in range(numCourses):
            if colors[s] == black or not nodes[s]:
                colors[s] = black
                continue

            stack = [s]
            while stack:
                v = stack.pop()
                if colors[v] == white:
                    colors[v] = grey
                    stack.append(v)
                    for w in nodes[v]:
                        if colors[w] == white:
                            stack.append(w)
                        if colors[w] == grey:
                            return False
                elif colors[v] == grey:
                    colors[v] = black
        return True


def test():
    s = Solution()
    print(s.canFinish(numCourses=3, prerequisites=[[1, 0]]))
    print(s.canFinish(numCourses=3, prerequisites=[[1, 0], [0, 1]]))


if __name__ == '__main__':
    test()
