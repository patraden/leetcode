from typing import List
from queue import SimpleQueue


class Solution:
    alphabet = 'ACGT'

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        distances = {startGene: 0}
        visited = {startGene}
        q = SimpleQueue()
        q.put(startGene)

        while q.qsize() > 0:
            s = q.get()
            for i in range(len(s)):
                for c in self.alphabet:
                    if c == s[i]:
                        continue

                    w = s[:i] + c + s[i + 1:]
                    if w in bank and w not in visited:
                        distances[w] = distances[s] + 1
                        visited.add(w)
                        q.put(w)

        if endGene not in distances:
            return -1

        return distances[endGene]


def test():
    s = Solution()
    print(s.minMutation(
        startGene="AACCGGTT",
        endGene="AACCGGTA",
        bank=["AACCGGTA"]
    ))
    print(s.minMutation(
        startGene="AACCGGTT",
        endGene="AAACGGTA",
        bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    ))


if __name__ == '__main__':
    test()
