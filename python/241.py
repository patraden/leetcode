from typing import List
from functools import cache


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def func(e: str) -> List[int]:
            if all(symbol not in e for symbol in "+-*"):
                return [int(e)]
            res = []
            for i, c in enumerate(e):
                if c in "-+*":
                    for e1 in func(e[:i]):
                        for e2 in func(e[i+1:]):
                            if c == "*":
                                elem = e1 * e2
                            elif c == "+":
                                elem = e1 + e2
                            else:
                                elem = e1 - e2
                            res.append(elem)
            return res
        return func(expression)


def test():
    s = Solution()
    expr = "1-4"
    res = s.diffWaysToCompute(expr)
    print(res)
    expr = "2-1-1"
    res = s.diffWaysToCompute(expr)
    print(res)
    expr = "2*3-4*5"
    res = s.diffWaysToCompute(expr)
    print(res)


if __name__ == '__main__':
    test()
