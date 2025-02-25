class Solution:
    def findNthDigit(self, n: int) -> int:
        start = 1
        num_digits = 1
        total_digits = 0
        while n > total_digits:
            qty = start * 9 * num_digits
            num_digits += 1
            start *= 10
            total_digits += qty
            # mind last iteration in while
            if n == total_digits:
                return int(str(start - 1)[-1])
            if n < total_digits:
                start //= 10
                total_digits -= qty
                num_digits -= 1
                break

        remainder = n - total_digits - 1
        num = start + remainder // num_digits
        digit = remainder % num_digits
        return int(str(num)[digit])


def test():
    s = Solution()
    for i in range(1, 210):
        print(s.findNthDigit(i))


if __name__ == '__main__':
    test()
