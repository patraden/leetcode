from typing import List


class Solution:
    q = 1000_000_007
    mod = 2 ** 32

    def hash(self, s):
        res = 0
        for c in s:
            res *= self.q
            res += ord(c)
            res %= self.mod
        return res

    def generate_hashes(self, s, length):
        if len(s) >= length:
            pw = (self.q ** (length - 1)) % self.mod
            res = [self.hash(s[:length])]
            for i in range(1, len(s) - length + 1):
                _hash = ((res[-1] - ord(s[i - 1]) * pw) * self.q + ord(s[i + length - 1])) % self.mod
                res.append(_hash)
            return res

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len(words[0])
        unique_words = set(words)
        d, res = {}, []
        for w in words:
            h = self.hash(w)
            d[h] = d.get(h, 0) + 1

        _hashes = self.generate_hashes(s, length)
        _long_hashes = self.generate_hashes(s, length * len(words))
        long_hashes_found = set()
        if not _long_hashes:
            return res
        for i in range(len(_long_hashes)):
            if _hashes[i] in d:
                # little optimization for possible repetitions
                if _long_hashes[i] in long_hashes_found:
                    res.append(i)
                    continue

                acc = {}
                j, k = i, 0
                while k < len(words) and j < len(_hashes):
                    h = _hashes[j]
                    if h in d and acc.get(h, 0) < d[h] and s[j:j + length] in unique_words:
                        acc[h] = acc.get(h, 0) + 1
                    else:
                        break
                    j += length
                    k += 1
                if k == len(words):
                    res.append(i)
                    long_hashes_found.add(_long_hashes[i])
        return res


def main():
    print(Solution().findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))
    print(Solution().findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))
    print(Solution().findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]))
    print(Solution().findSubstring(s="mississippi", words=["mississippis"]))

    with open('input.txt', 'r') as f:
        s = f.readline().rstrip()
        words = f.readline().rstrip().split(',')
    print(Solution().findSubstring(s=s, words=words))


if __name__ == "__main__":
    main()

