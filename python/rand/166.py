class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator * denominator < 0 else ""

        numerator = abs(numerator)
        denominator = abs(denominator)

        res = f"{sign}{numerator // denominator}"
        r = numerator % denominator

        if r == 0:
            return res
        res += "."

        unique = {}
        seq = []
        idx = -1
        while r > 0:
            if r in unique:
                res += ''.join(str(n) for n in seq[:unique[r] + 1])
                res += f"({''.join(str(n) for n in seq[unique[r] + 1:])})"
                return res

            unique[r] = idx
            while r < denominator:
                r *= 10
                idx += 1
                unique[r] = idx
                seq.append(0)

            seq[idx] = r // denominator
            r %= denominator

        res += ''.join(str(n) for n in seq)
        return res


def test():
    print(Solution().fractionToDecimal(2, 7))
    print(Solution().fractionToDecimal(1, 9))
    print(Solution().fractionToDecimal(1, 2))
    print(Solution().fractionToDecimal(2, 1))
    print(Solution().fractionToDecimal(4, 333))
    print(Solution().fractionToDecimal(1 + 50 * 900, 900))
    print(Solution().fractionToDecimal(719, 990))
    print(Solution().fractionToDecimal(1, -8))


if __name__ == '__main__':
    test()
