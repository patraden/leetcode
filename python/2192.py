from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        nodes = [[] for _ in range(n)]
        parents = [[] for _ in range(n)]
        res = [[] for _ in range(n)]

        for w, u in edges:
            nodes[u].append(w)
            parents[w].append(u)

        white, grey, black = 0, 1, 2
        colors = [white] * n

        for i in range(n):
            stack = [i]
            while stack:
                u = stack.pop()
                if colors[u] == white:
                    colors[u] = grey
                    stack.append(u)
                    for w in nodes[u]:
                        if colors[w] == white:
                            stack.append(w)
                elif colors[u] == grey:
                    for p in parents[u]:
                        res[p] += res[u]
                        res[p].append(u)
                        res[p] = sorted(set(res[p]))
                    colors[u] = black
        # print(res)
        return res


def test():
    Solution().getAncestors(n=8, edges=[
        [0, 3], [0, 4], [1, 3],
        [2, 4], [2, 7], [3, 5],
        [3, 6], [3, 7], [4, 6]
    ])
    Solution().getAncestors(n=5, edges=[
        [0, 1], [0, 2], [0, 3],
        [0, 4], [1, 2], [1, 3],
        [1, 4], [2, 3], [2, 4],
        [3, 4]
    ])


if __name__ == '__main__':
    test()
