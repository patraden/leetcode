class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n % 2
            n >>= 1
        return res



def test():
    print(Solution().hammingWeight(0))
    print(Solution().hammingWeight(1))
    print(Solution().hammingWeight(11))
    print(Solution().hammingWeight(128))
    print(Solution().hammingWeight(2147483645))


if __name__ == '__main__':
    test()
