from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        acc = {}
        for c in words[0]:
            acc[c] = acc.get(c, 0) + 1

        for word in words[1:]:
            h = {}
            for c in word:
                h[c] = h.get(c, 0) + 1

            acc_new = {}
            for k in acc:
                if k in h:
                    acc_new[k] = min(h[k], acc[k])

            acc = acc_new

            if len(acc) == 0:
                return []

        res = []
        for k in acc:
            for i in range(acc[k]):
                res.append(k)

        return res


def test():
    print(Solution().commonChars(words=["bella", "label", "roller"]))
    print(Solution().commonChars(words = ["cool","lock","cook"]))


if __name__ == '__main__':
    test()
