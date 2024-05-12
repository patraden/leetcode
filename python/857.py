from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n, h = len(quality), []
        u = sorted([(wage[i] / quality[i], -quality[i]) for i in range(n)])

        umx = u[k - 1][0]
        qsum = 0

        for j in range(k):
            qsum -= u[j][1]
            heapq.heappush(h, u[j][1])

        res = qsum * umx
        for i in range(k, n):
            qmx = -heapq.heappop(h)
            q = -u[i][1]
            res = min(res, (qsum - qmx + q) * u[i][0])
            qsum += (q - qmx)
            heapq.heappush(h, -q)

        return res


def test():
    print(Solution().mincostToHireWorkers(quality=[10, 20, 5], wage=[70, 50, 30], k=2))
    print(Solution().mincostToHireWorkers(quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], k=3))
    print(Solution().mincostToHireWorkers(
        quality=[32, 43, 66, 9, 94, 57, 25, 44, 99, 19],
        wage=[187, 366, 117, 363, 121, 494, 348, 382, 385, 262],
        k=4))


if __name__ == '__main__':
    test()
