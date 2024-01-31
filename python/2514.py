import math


class Solution:
    MOD = 1000_000_007

    def countPermutations(self, word: str) -> int:
        n = len(word)
        h = {}
        for char in word:
            h[char] = h.get(char, 0) + 1

        res = 1
        m = n
        for char in h:
            k = h[char]
            res *= math.comb(m, k)
            res %= self.MOD
            m -= k

        return res

    def countAnagrams(self, s: str) -> int:
        res = 1
        for word in s.split(' '):
            res *= self.countPermutations(word)
            res %= self.MOD
        return res


def test():
    print(Solution().countAnagrams("abbbss"))
    print(Solution().countAnagrams("aa"))
    print(Solution().countAnagrams(s="too hot"))


if __name__ == '__main__':
    test()
