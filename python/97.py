class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        prv = [True] + [False] * m
        for j in range(1, m + 1):
            prv[j] = prv[j - 1] and s2[j - 1] == s3[j - 1]

        if n == 0:
            return prv[m]

        for i in range(n):
            nxt = [False] * (m + 1)
            for j in range(m + 1):
                nxt[j] = (
                        (j == 0 and prv[j] and s1[i] == s3[i]) or
                        (j > 0 and prv[j] and s1[i] == s3[i + j]) or
                        (j > 0 and nxt[j - 1] and s2[j - 1] == s3[i + j])
                )
            prv = nxt.copy()
        return nxt[m]


def test():
    print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
    print(Solution().isInterleave(s1="bcdk", s2="", s3="bcdk"))
    print(Solution().isInterleave(s1="", s2="", s3=""))


if __name__ == '__main__':
    test()
