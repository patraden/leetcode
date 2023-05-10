class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        m, n = len(s), len(p)
        dp[i, j] = isMatch(s[:i], p[:j])
        dp[0, 0] = isMatch(s[:0], p[:0]) = True
        dp[n, m] = isMatch(s[:n], p[:m]) contains the answer
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        #  if string is empty:
        #  overall pattern containing .* or a* subpattern will return True
        #  as long as the pattern without subpattern is valid
        #  Every other subpattern will be faulty
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # we add 1 character to a string first
        # then we iterate through pattern (j - 1) index is used as we extended we array to m + 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if we have simple subpattern like '.' or 'a' and it matches character in the string
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # if we have simple subpattern like '.*' or 'a*'
                # then we first account if there is a match for pattern without this subpattern (match to empty string)
                # and then check if it matches character in the string
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] |= dp[i - 1][j]
        return dp[m][n]


def main():
    pass


if __name__ == "__main__":
    main()
