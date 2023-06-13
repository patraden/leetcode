def is_match(s: str, p: str) -> bool:
    mem = {}

    def dp(i, j):
        if (i, j) not in mem:
            if j == len(p):  # Check if pattern is empty, if so string s should also be empty
                mem[(i, j)] = i == len(s)
            else:
                # Check the first character match in s and pattern
                # String should not be empty
                # The first characters exactly match (Or)
                # pattern's first char contains "." to match any char in s
                is_first_char_match = len(s) > i and (s[i] == p[j] or p[j] == ".")

                # When '*' is present in the second char of pattern
                if j < len(p) - 1 and p[j + 1] == "*":
                    mem[(i, j)] = dp(i, j + 2) or (is_first_char_match and dp(i + 1, j))
                else:
                    # Continue checking the remaining characters using recursion
                    mem[(i, j)] = is_first_char_match and dp(i + 1, j + 1)

        return mem[(i, j)]

    return dp(0, 0)


def main():
    print(is_match(s='aaa', p='a*aaa'))


if __name__ == "__main__":
    main()
