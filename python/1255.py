from collections import defaultdict
from typing import List
from string import ascii_lowercase


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        scores = dict(zip(ascii_lowercase, score))
        h = defaultdict(int)
        for c in letters:
            h[c] += 1

        def contains(w, store):
            acc = defaultdict(int)
            sc = 0
            for c in w:
                acc[c] += 1
                sc += scores[c]
                if c not in store or store[c] - acc[c] < 0:
                    return None, None
            return acc, sc

        valid_words = []
        for word in words:
            _acc, _ = contains(word, h)
            if _acc:
                valid_words.append(word)

        res = 0

        def helper(i, d, s=0):
            nonlocal res
            for j in range(i, len(valid_words)):
                w = valid_words[j]
                acc, sc = contains(w, d)
                if acc:
                    res = max(res, s + sc)
                    for k in acc:
                        d[k] -= acc[k]
                    helper(j + 1, d, s + sc)
                    for k in acc:
                        d[k] += acc[k]

        helper(0, h.copy())
        return res


def test():
    print(Solution().maxScoreWords(
        words=["dog", "cat", "dad", "good"],
        letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
        score=[1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ))
    print(Solution().maxScoreWords(
        words=["xxxz", "ax", "bx", "cx"],
        letters=["z", "a", "b", "c", "x", "x", "x"],
        score=[4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]
    ))
    print(Solution().maxScoreWords(
        words=["baa", "bba", "ccb", "ac"],
        letters=["a", "b", "b", "b", "b", "c"],
        score=[2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ))


if __name__ == '__main__':
    test()
