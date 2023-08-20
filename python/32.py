class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0

        stack = []  # keep only open brackets
        start = -1
        final = cur = 0
        for i in range(len(s)):
            if s[i] == ')':
                if not stack:
                    start = i
                    final = max(final, cur)
                    cur = 0
                    continue
                stack.pop()
                if not stack:
                    cur += (i - start)
                    start = i
            else:
                stack.append(i)

        final = max(cur, final)
        i = len(s)
        while stack:
            final = max(i - stack[-1] - 1, final)
            i = stack.pop()
        return final


def main():
    print(Solution().longestValidParentheses('()((())(((('))
    print(Solution().longestValidParentheses(')()())'))
    print(Solution().longestValidParentheses(''))


if __name__ == "__main__":
    main()
