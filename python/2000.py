class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        return word[:idx + 1][::-1] + word[idx + 1:]


def test():
    print(Solution().reversePrefix(word="abcdefd", ch="d"))
    print(Solution().reversePrefix(word="xyxzxe", ch="z"))
    print(Solution().reversePrefix(word="abcd", ch="z"))
    print(Solution().reversePrefix(word="z", ch="z"))


if __name__ == '__main__':
    test()
