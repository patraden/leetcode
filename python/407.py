from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import heapq

        ans = 0
        n, m  = len(heightMap), len(heightMap[0])
        if n <= 2 or m <= 2:
            return ans

        border = []
        visited = set()


        # init heap
        for i in range(n):
            heapq.heappush(border, (heightMap[i][0], i, 0))
            heapq.heappush(border, (heightMap[i][m - 1], i, m - 1))
            visited.add((i, 0))
            visited.add((i, m - 1))
        
        for j in range(1, m-1):
            heapq.heappush(border, (heightMap[0][j], 0, j))
            heapq.heappush(border, (heightMap[n-1][j], n - 1, j))
            visited.add((0, j))
            visited.add((n - 1, j))


        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
        while len(visited) < n * m:
            h, i, j = heapq.heappop(border)
            for (di, dj) in dirs:
                if 0 <= i + di < n and 0 <= j + dj < m and (i + di, j + dj) not in visited:
                    if heightMap[i+di][j+dj] < h:
                        ans += h - heightMap[i+di][j+dj]
                        heapq.heappush(border, (h, i+di, j+dj))
                    else:
                        heapq.heappush(border, (heightMap[i+di][j+dj], i+di, j+dj))
                    visited.add((i+di, j+dj))

        return ans


def test():
    heightMap = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]
    assert Solution().trapRainWater(heightMap) == 4

    heightMap = [
        [3, 3, 3, 3, 3],
        [3, 2, 2, 2, 3],
        [3, 2, 1, 2, 3],
        [3, 2, 2, 2, 3],
        [3, 3, 3, 3, 3]
    ]
    assert Solution().trapRainWater(heightMap) == 10

    heightMap = [
        [12, 13, 1, 12],
        [13, 4, 13, 12],
        [13, 8, 10, 12],
        [12, 13, 12, 12],
        [13, 13, 13, 13]
    ]
    assert Solution().trapRainWater(heightMap) == 14


if __name__ == '__main__':
    test()
