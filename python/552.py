class Solution:
    memo = {}

    def checkRecord(self, n: int) -> int:
        """
        0 - no 'A', last 'P'
        1 - no 'A', last 'L'
        2 - no 'A', last 'LL'
        3 - 'A', last 'A'
        4 - 'A', last 'P'
        5 - 'A', last 'L'
        6 - 'A', last 'LL'
        """
        if n in self.memo:
            return self.memo[n]

        mod = 10 ** 9 + 7
        acc = [1, 1, 0, 1, 0, 0, 0]
        i = 1
        while i < n:
            self.memo[i] = sum(acc) % mod
            acc_new = [0] * 7
            acc_new[0] = sum(acc[:3]) % mod
            acc_new[1] = acc[0]
            acc_new[2] = acc[1]
            acc_new[3] = sum(acc[:3]) % mod
            acc_new[4] = sum(acc[3:]) % mod
            acc_new[5] = sum(acc[3:5]) % mod
            acc_new[6] = acc[5]
            acc = acc_new
            i += 1

        self.memo[n] = sum(acc) % mod
        return self.memo[n]


def test():
    print(Solution().checkRecord(1))
    print(Solution().checkRecord(2))
    print(Solution().checkRecord(10101))


if __name__ == '__main__':
    test()
