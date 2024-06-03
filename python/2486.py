from typing import List


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx = 0
        for c in s:
            if idx < len(t) and c == t[idx]:
                idx += 1
        return len(t[idx:])


def test():
    print(Solution().appendCharacters(s="coaching", t="coding"))
    print(Solution().appendCharacters(s="abcde", t="a"))
    print(Solution().appendCharacters(s="z", t="abcde"))


if __name__ == '__main__':
    test()
