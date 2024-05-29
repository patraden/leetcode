class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        num = int(s, 2)
        while num > 1:
            if num % 2 == 0:
                num >>= 1
                res += 1
            else:
                num += 1
                res += 1
        return res


def test():
    print(Solution().numSteps(s="1101"))
    print(Solution().numSteps(s="10"))
    print(Solution().numSteps(s="1"))


if __name__ == '__main__':
    test()
