from string import digits


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        p = 0  # prefix length
        stack = []
        tstart = tcurrent = decoded = 0
        while tcurrent < len(s):
            if s[tcurrent] in digits:
                word = s[tstart:tcurrent]
                j = 1
                digit = int(s[tcurrent])
                while (tcurrent + j) < len(s) and s[tcurrent + j] in digits and k > (p + len(word)) * digit:
                    digit *= int(s[tcurrent + j])
                    j += 1

                stack.append((p, word, digit))
                p = (p + len(word)) * digit

                #  main algo start
                if k <= p:
                    index = (k - 1)
                    while stack:
                        p, word, digit = stack.pop()
                        index %= (p + len(word))
                        if index >= p:
                            return word[index - p]
                #  main algo end

                tcurrent += j
                tstart = tcurrent
                decoded = p
            elif decoded == k - 1:
                return s[tcurrent]
            else:
                tcurrent += 1
                decoded += 1


def main():
    print(Solution().decodeAtIndex(s="leet2code3", k=13))
    print(Solution().decodeAtIndex(s="ha22", k=5))
    print(Solution().decodeAtIndex(s="a2345678999999999999999", k=3))
    print(Solution().decodeAtIndex(s="abc", k=1))


if __name__ == "__main__":
    main()
