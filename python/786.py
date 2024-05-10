from typing import List
import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = [(arr[0] / arr[i], 0, i) for i in range(len(arr) - 1, 0, -1)]

        e = 0
        while e < k:
            _, i, j = heapq.heappop(h)
            if i + 1 < j:
                heapq.heappush(h, (arr[i + 1] / arr[j], i + 1, j))
            e += 1

        return [arr[i], arr[j]]


def test():
    print(Solution().kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3))
    print(Solution().kthSmallestPrimeFraction(arr=[1, 7], k=1))


if __name__ == '__main__':
    test()
