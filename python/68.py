from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        sep = ' '
        i = 0
        ans = []
        while i < len(words):
            line = [words[i]]
            chars = len(words[i])
            i += 1
            while i < len(words) and len(words[i]) + 1 <= (maxWidth - chars - (len(line) - 1)):
                line.append(words[i])
                chars += len(words[i])
                i += 1

            ws = maxWidth - chars
            if i >= len(words):  # last line
                res = sep.join(line)
                ws -= len(line) - 1
                if ws > 0:
                    res += sep * ws
            elif len(line) == 1:
                res = line[0]
                res += sep * ws
            else:
                res = ""
                m = len(line) - 1
                r = ws % m
                d = ws // m

                for j in range(len(line)):
                    res += line[j]
                    if j < (len(line) - 1):
                        res += sep * d
                        if r > 0:
                            res += sep
                            r -= 1
            ans.append(res)
        return ans


def test():
    Solution().fullJustify(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16
    )

    print("=" * 40)

    Solution().fullJustify(
        words=["What", "must", "be", "acknowledgment", "shall", "be"],
        maxWidth=16
    )

    print("=" * 40)

    Solution().fullJustify(
        words=["Science", "is", "what", "we", "understand", "well", "enough", "to",
               "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"],
        maxWidth=20
    )


if __name__ == '__main__':
    test()
