class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        key = res = 0
        cm = {'': 0}
        d = {key: 1}

        num = 1
        for c in 'abcdefghij':
            cm[c] = num
            num <<= 1

        for w in word:
            key ^= cm[w]
            # count 0 odd
            res += d.get(key, 0)
            # count 1 odd
            for v in cm.values():
                if v != 0:
                    res += d.get(key ^ v, 0)
            d[key] = d.get(key, 0) + 1

        return res


def test():
    print(Solution().wonderfulSubstrings(word="aabb"))
    print(Solution().wonderfulSubstrings(word="he"))
    print(Solution().wonderfulSubstrings(word="acabb"))
    print(Solution().wonderfulSubstrings(word="ba"))
    print(Solution().wonderfulSubstrings(word="ehaehcjjaafjdceac"))


if __name__ == '__main__':
    test()
