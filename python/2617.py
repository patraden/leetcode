from typing import List


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        import heapq
        n, m = len(grid), len(grid[0])
        cols = [[] for _ in range(m)]

        _min = -1
        for i in range(n):
            row = [] if i > 0 else [(0, 0, -1, 1)]
            for j in range(m):
                #  getting min from col
                col = cols[j]
                while len(col) > 0 and col[0][1] + col[0][3] < i:
                    heapq.heappop(col)
                #  getting min from row
                while len(row) > 0 and row[0][2] + row[0][3] < j:
                    heapq.heappop(row)

                #  get the minimum path
                if len(col) > 0 and len(row) > 0:
                    _min = min(col[0][0], row[0][0]) + 1
                elif len(col) > 0:
                    _min = col[0][0] + 1
                elif len(row) > 0:
                    _min = row[0][0] + 1
                else:
                    _min = -1

                #  if next element is reachable from current then add it to row and col queues
                if grid[i][j] > 0 and _min > 0:
                    heapq.heappush(row, (_min, i, j, grid[i][j]))
                    heapq.heappush(col, (_min, i, j, grid[i][j]))
        return _min


def main():
    with open("input.txt", mode='r') as f:
        n = int(f.readline().rstrip())
        m = int(f.readline().rstrip())
        mat = [[int(e) for e in f.readline().rstrip().split()] for _ in range(n)]
        print(Solution().minimumVisitedCells(mat))


if __name__ == "__main__":
    main()
