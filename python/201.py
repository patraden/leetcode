def b(num):
    num |= num >> 1
    num |= num >> 2
    num |= num >> 4
    num |= num >> 8
    num |= num >> 16
    return num - (num >> 1)


class Solution:
    def major_bit(self, num):
        num |= num >> 1
        num |= num >> 2
        num |= num >> 4
        num |= num >> 8
        num |= num >> 16
        return num - (num >> 1)

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bit_left = self.major_bit(left)
        bit_right = self.major_bit(right)
        if bit_right > bit_left:
            return 0

        mask = bit_left
        while bit_left & left == bit_left & right and bit_left > 0:
            bit_left >>= 1
            mask |= bit_left
        return left & mask


def test():
    print(Solution().rangeBitwiseAnd(left=5, right=5))
    print(Solution().rangeBitwiseAnd(left=5, right=7))
    print(Solution().rangeBitwiseAnd(left=0, right=0))
    print(Solution().rangeBitwiseAnd(left=1, right=2147483647))
    print(bin(Solution().rangeBitwiseAnd(left=int('11010', 2), right=int('11111', 2))))


if __name__ == '__main__':
    test()
