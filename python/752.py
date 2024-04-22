from typing import List
from queue import SimpleQueue


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def moves(wheels: str):
            for i in range(len(wheels)):
                for delta in (1, -1):
                    digit = int(wheels[i])
                    yield wheels[:i] + str((digit + delta) % 10) + wheels[i + 1:]

        s = '0000'

        distances = {end: -1 for end in deadends}
        if s in distances:
            return -1
        distances[s] = 0

        q = SimpleQueue()
        q.put(s)

        while not q.empty():
            n = q.get()
            if n == target:
                return distances[n]
            for w in moves(n):
                if w not in distances:
                    q.put(w)
                    distances[w] = distances[n] + 1
        return -1


def test():
    print(Solution().openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))
    print(Solution().openLock(deadends=["8888"], target="0009"))
    print(Solution().openLock(deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target="8888"))
    print(Solution().openLock(deadends=["0000"], target="0000"))


if __name__ == '__main__':
    test()
