class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        stack = list(zip(s, locked))
        locks = 0
        for i in range(n):
            if stack[i] == (')', '1'):
                locks += 1
                if 2 * locks > i + 1:
                    return False

        locks = 0
        for i in range(n - 1, -1, -1):
            if stack[i] == ('(', '1'):
                locks += 1
                if 2 * locks > len(stack) - i:
                    return False

        return True


def main():
    print(Solution().canBeValid(s="))()))", locked="010100"))
    print(Solution().canBeValid(s="()()", locked="0000"))
    print(Solution().canBeValid(s="())", locked="000"))
    print(Solution().canBeValid(s="()", locked="00"))
    print(Solution().canBeValid(s=")(", locked="00"))
    print(Solution().canBeValid(s="(()())((((", locked="1111111100"))
    print(Solution().canBeValid(
        s="())()))()(()(((())(()()))))((((()())(())",
        locked="1011101100010001001011000000110010100101")
    )


if __name__ == "__main__":
    main()
