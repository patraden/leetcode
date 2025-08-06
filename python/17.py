from typing import List


class Solution:
    h = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits: str) -> List[str]:
        def btr(d, prefix=None):
            nonlocal res
            prefix = prefix or []

            if len(d) == 0:
                return

            if len(prefix) == len(d):
                v = ''.join(prefix)
                res.append(v)
                return

            i = int(d[len(prefix)])
            for c in self.h[i]:
                prefix.append(c)
                btr(d, prefix)
                prefix.pop()

        res = []
        btr(digits)

        return res


def test():
    s = Solution()
    test1 = s.letterCombinations("23")
    print(test1)
    test2 = s.letterCombinations("2")
    print(test2)
    test3 = s.letterCombinations("")
    print(test3)
    test4 = s.letterCombinations("239")
    print(test4)


if __name__ == '__main__':
    test()
