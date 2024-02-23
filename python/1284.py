from typing import List
import queue


class Matrix:
    def __init__(self, data: List[List[int]]):
        self.n = len(data)
        self.m = 0 if self.n == 0 else len(data[0])
        self.bin = "".join([str(elem) for row in data for elem in row]) if len(self) > 0 else None
        self.int = int(self.bin, 2) if self.bin else None
        self.masks = None
        self._generate_masks()

    def __len__(self):
        return self.n * self.m

    @property
    def masks_bin(self):
        return list(map(bin, self.masks))

    def _generate_masks(self) -> None:
        bits = []
        num = 2 ** (len(self) - 1)
        while num >= 1:
            bits.append(num)
            num >>= 1
        self.masks = bits.copy()

        for k in range(len(self)):
            i, j = k // self.m, k % self.m
            prv, nxt = k - 1, k + 1

            if 0 <= j - 1 < self.m:
                self.masks[k] += bits[prv]
            if 0 <= j + 1 < self.m:
                self.masks[k] += bits[nxt]

            prv, nxt = k - self.m, k + self.m
            if 0 <= i - 1 < self.n:
                self.masks[k] += bits[prv]
            if 0 <= i + 1 < self.n:
                self.masks[k] += bits[nxt]



class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        # your algo here
        m = Matrix(mat)
        q = queue.SimpleQueue()
        q.put(m.int)
        distance = {m.int: 0}
        while q.qsize() > 0:
            s = q.get()
            if s == 0:
                return distance[s]
            for mask in m.masks:
                w = s ^ mask
                if w not in distance:
                    q.put(w)
                    distance[w] = distance[s] + 1
        return -1


def test():
    print(Solution().minFlips(mat=[
        [0, 0],
        [0, 1]
    ]))
    print(Solution().minFlips(mat=[
        [0]
    ]))
    print(Solution().minFlips(mat=[
        [1, 0, 0],
        [1, 0, 0]
    ]))
    print(Solution().minFlips(mat=[
        [1, 1, 1],
        [1, 0, 1],
        [0, 0, 0]
    ]))


if __name__ == '__main__':
    test()
