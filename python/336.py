from typing import List


class Solution:
    Q = 1000_000_007
    MOD = 2 ** 32
    NULL_HASH = -1

    @staticmethod
    def is_palindrome(word) -> bool:
        for i in range(len(word) // 2):
            if word[i] != word[len(word) - 1 - i]:
                return False
        return True

    def determine_all_hashes(self, words) -> tuple:
        left, right = {}, {}
        hash_prefixes = [None] * len(words)

        for k, word in enumerate(words):
            lp = rp = 0
            wp = []
            q = 1
            for i in range(len(word)):
                l, r = i, len(word) - 1 - i

                lp += ord(word[l]) * q
                lp %= self.MOD
                rp += ord(word[r]) * q
                rp %= self.MOD
                q = (q * self.Q) % self.MOD

                wp.append((lp, rp, q))

            assert lp not in left, "custom hash collision"
            assert rp not in right, "custom hash collision"

            if len(word) == 0:
                left[self.NULL_HASH] = k
                right[self.NULL_HASH] = k
            else:
                left[lp] = k
                right[rp] = k
            hash_prefixes[k] = wp
        return left, right, hash_prefixes

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        left, right, hash_prefixes = self.determine_all_hashes(words)
        res = []
        found = set()

        for w in range(len(words)):
            # empty string handling
            if len(hash_prefixes[w]) == 0:
                for v in range(len(words)):
                    if v != w:
                        left_pref, right_pref, _ = hash_prefixes[v][-1]
                        if left_pref == right_pref and self.is_palindrome(words[v]):
                            res.append([v, w])
                            res.append([w, v])
            #  word's left, right prefix hashes and max polynomial q power + 1
            for left_pref, right_pref, pref_q in hash_prefixes[w]:
                if left_pref in right and right[left_pref] != w:
                    # index of the pair word
                    v = right[left_pref]
                    # reversed prefix hash
                    left_pref_rev, _, _ = hash_prefixes[v][-1]
                    # word's left and right hashes and max polynomial q power + 1
                    left_word, right_word, word_q = hash_prefixes[w][-1]
                    # check if concatenation of w and v is a palindrome
                    left_concat = (left_word + left_pref_rev * word_q) % self.MOD
                    right_concat = (right_word * pref_q + left_pref) % self.MOD
                    if left_concat == right_concat and self.is_palindrome(words[w] + words[v]):
                        if (v, w) not in found:
                            res.append([w, v])
                            found.add((w, v))

                if right_pref in left and left[right_pref] != w:
                    # index of the pair word
                    v = left[right_pref]
                    # reversed prefix hash
                    _, right_pref_rev, _ = hash_prefixes[v][-1]
                    # word's left and right hashes and max polynomial q power + 1
                    left_word, right_word, word_q = hash_prefixes[w][-1]
                    # check if concatenation of w and v is a palindrome
                    left_concat = (right_pref + left_word * pref_q) % self.MOD
                    right_concat = (right_word + right_pref_rev * word_q) % self.MOD
                    if left_concat == right_concat and self.is_palindrome(words[v] + words[w]):
                        if (v, w) not in found:
                            res.append([v, w])
                            found.add((v, w))
        return res


def main():
    print(Solution().palindromePairs(words=["abcd", "dcba", "lls", "s", "sssll"]))
    print(Solution().palindromePairs(words=["bat", "tab", "cat"]))
    print(Solution().palindromePairs(words=["a", ""]))
    print(Solution().palindromePairs(words=["a", "b", "c", "ab", "ac", "aa"]))


if __name__ == "__main__":
    main()
