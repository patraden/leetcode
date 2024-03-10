class Solution:
    def totalNQueens(self, n: int) -> int:
        done = 2 ** n - 1
        half_done = 2 ** ((n + 1) // 2) - 1
        count = 0
        res = []

        def solve(ld, col, rd):
            nonlocal done, half_done, count
            if col == done:
                count += 1
                if res[0] < n // 2 + 1:  # symmetric solution for 0-row
                    count += 1
                return
            pos = ~ (col | ld | rd)
            while pos & (half_done if col == 0 else done):
                bit = pos & -pos
                pos -= bit
                res.append(bit.bit_length())
                solve((ld | bit) >> 1, col | bit, (rd | bit) << 1)
                res.pop()

        solve(0, 0, 0)
        return count


def test():
    print(Solution().totalNQueens(n=3))


if __name__ == '__main__':
    test()
