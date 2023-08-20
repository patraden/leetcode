class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        stack, n, qty_letters = [], len(s), 0
        right = [(n, qty_letters)] * n
        for i in range(n - 1, -1, -1):
            if s[i] == letter:
                qty_letters += 1
            while stack and s[i] <= s[stack[-1][0]]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append((i, qty_letters))

        print(right)

        return ""


def main():
    print(Solution().smallestSubsequence(s="leet", k=3, letter="e", repetition=1))


if __name__ == "__main__":
    main()
