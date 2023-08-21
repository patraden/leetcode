class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        stack, n, lts = [], len(s), 0
        next_smaller = [n] * n
        repetitions = [0] * n
        for i in range(n - 1, -1, -1):
            if s[i] == letter:
                lts += 1
            while stack and s[i] <= s[stack[-1]]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)
            repetitions[i] = lts

        lts = cur = 0
        res = ""
        while len(res) < k and cur < n:
            nxt = next_smaller[cur]
            nxt_rps = repetitions[nxt] if nxt < n else 0
            reps_reminder = 0 if (repetition - lts) < 0 else (repetition - lts)
            if reps_reminder < (k - len(res)) <= (n - nxt) and nxt_rps >= reps_reminder:
                cur = nxt
            elif reps_reminder == (k - len(res)):
                if s[cur] == letter:
                    res += s[cur]
                    lts += 1
                cur += 1
            else:
                if s[cur] == letter:
                    lts += 1
                res += s[cur]
                cur += 1
        return res


def main():
    print(Solution().smallestSubsequence(s="leet", k=3, letter="e", repetition=1))
    print(Solution().smallestSubsequence(s="leetcode", k=4, letter="e", repetition=2))
    print(Solution().smallestSubsequence(s="bb", k=2, letter="b", repetition=2))
    print(Solution().smallestSubsequence(s="bbattbaaab", k=5, letter="b", repetition=2))


if __name__ == "__main__":
    main()
