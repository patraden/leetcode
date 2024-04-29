from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = [[] for _ in range(n)]
        for u, v in edges:
            nodes[u].append(v)
            nodes[v].append(u)

        dp = [0] * n
        qty = [0] * n

        def sum_root_paths(root=0, parent=None):
            #  this is a leave
            if len(nodes[root]) == 1 and parent is not None and nodes[root][0] == parent:
                dp[root] = 0
                qty[root] = 1
                return

            _s = _q = 0
            for w in nodes[root]:
                if w != parent:
                    sum_root_paths(w, root)
                    _s += dp[w]
                    _q += qty[w]
            dp[root] = _s + _q
            qty[root] = 1 + _q

        sum_root_paths()

        def sum_paths(current=0, parent=None):
            if parent is not None:
                parent_s = dp[parent]
                current_q = qty[current]
                dp[current] = parent_s + n - 2 * current_q
            for w in nodes[current]:
                if w != parent:
                    sum_paths(w, current)

        sum_paths()
        return dp


def test():
    print(Solution().sumOfDistancesInTree(n=6, edges=[[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
    print(Solution().sumOfDistancesInTree(n=3, edges=[[0, 1], [0, 2]]))
    print(Solution().sumOfDistancesInTree(n=2, edges=[[1, 0]]))
    print(Solution().sumOfDistancesInTree(n=1, edges=[]))


if __name__ == '__main__':
    test()
