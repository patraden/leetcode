class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:

        dict_word1, dict_word2 = {}, {}
        for _ in word1:
            dict_word1[_] = dict_word1.get(_, 0) + 1

        for _ in word2:
            dict_word2[_] = dict_word2.get(_, 0) + 1

        if abs(len(dict_word1) - len(dict_word2)) > 2:
            return False

        dict_word1_len = len(dict_word1)
        dict_word2_len = len(dict_word2)

        for l in dict_word1:
            for r in dict_word2:
                word1_len = dict_word1_len
                word2_len = dict_word2_len
                if l != r:
                    if dict_word1[l] == 1:
                        word1_len -= 1
                    if l not in dict_word2:
                        word2_len += 1

                    if dict_word2[r] == 1:
                        word2_len -= 1
                    if r not in dict_word1:
                        word1_len += 1

                if word1_len == word2_len:
                    return True

        return False


def test():
    assert Solution().isItPossible(word1="ac", word2="b") is False
    assert Solution().isItPossible(word1="abcc", word2="aab") is True
    assert Solution().isItPossible(word1="abcde", word2="fghij") is True
    assert Solution().isItPossible(word1="aa", word2="ab") is False


if __name__ == '__main__':
    test()
