class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        from math import sqrt, floor
        for i in range(floor(sqrt(c)) + 1):
            if sqrt(c - i * i).is_integer():
                return True
        return False


def test():
    print(Solution().judgeSquareSum(0))
    print(Solution().judgeSquareSum(3))
    print(Solution().judgeSquareSum(5))
    print(Solution().judgeSquareSum(1308917), bin(1308917))


if __name__ == '__main__':
    test()
