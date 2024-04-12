class Solution:
    def reverseBits(self, n: int) -> int:
        res = ""
        while n > 0:
            res += str(n % 2)
            n >>= 1

        res += "0" * (32 - len(res))
        return int(res, 2)


def test():
    print(Solution().reverseBits(43261596))
    print(Solution().reverseBits(4294967293))


if __name__ == '__main__':
    test()
