from typing import List
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n

        for edge in roads:
            degree[edge[0]] += 1
            degree[edge[1]] += 1

        degree.sort()

        value = 1
        total_importance = 0
        for d in degree:
            total_importance += value * d
            value += 1

        return total_importance


def test():
    print(Solution().maximumImportance(n=5, roads=[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
    print(Solution().maximumImportance(n=5, roads=[[0, 3], [2, 4], [1, 3]]))
    print(Solution().maximumImportance(n=5, roads=[[0, 1]]))


if __name__ == '__main__':
    test()
