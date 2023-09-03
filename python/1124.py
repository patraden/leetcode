from typing import List


class Solution:
    def longestWPI_square(self, hours: List[int]) -> (int, int, int):
        n = len(hours)
        res = []
        for i in range(n):
            prefix = 0
            for j in range(i, n):
                prefix += int(hours[j] > 8)
                if 2 * prefix > (j - i + 1):
                    res.append(j + 1 - i)
        return max(res)

    def longestWPI(self, hours: List[int]) -> int:
        prefix = 0
        d = {prefix: -1}
        res = 0
        for i in range(len(hours)):
            prefix += (1 if hours[i] > 8 else -1)
            if prefix > 0:
                res = i + 1
            elif prefix not in d:
                d[prefix] = i
            elif (prefix - 1) in d:
                res = max(res, i - d[prefix - 1])
        return res


def main():
    print(Solution().longestWPI(hours=[9, 9, 0, 9, 9, 4, 7, 9, 7, 9, 0, 9, 1]))
    print(Solution().longestWPI(hours=[9, 9, 6, 0, 6, 6, 9]))
    print(Solution().longestWPI(hours=[6, 6, 6]))
    print(Solution().longestWPI(hours=[6, 8, 7, 9, 9]))
    print(Solution().longestWPI(hours=[9, 6, 9]))
    print(Solution().longestWPI(hours=[9, 9, 9]))
    print(Solution().longestWPI(hours=[6, 7, 9, 9]))
    print(Solution().longestWPI(hours=[8, 10, 6, 16, 5]))
    print(Solution().longestWPI(hours=[5, 5, 9, 9, 5, 6, 10, 8, 8, 10, 5, 5, 7]))  # 5
    print(Solution().longestWPI(hours=[5, 5, 2, 3, 9, 9, 10, 8, 8, 10, 5, 5, 7]))  # 5
    hours = [11, 2, 4, 14, 2, 15, 7, 10, 1, 16, 9, 0, 2, 8, 4, 14, 6, 12, 2, 8, 6, 4, 14, 13, 7, 16, 14, 2, 3, 2, 8, 3,
             12, 3, 3, 9, 14, 1, 5, 3, 12, 0, 15, 5, 0, 2, 3, 16, 7, 2, 1, 1, 4, 9, 0, 11, 9, 16, 15, 7, 0, 5, 6, 4, 12,
             1, 1, 2, 13, 8, 3, 9, 12, 9, 3, 11, 4, 14, 7, 5, 16, 0, 11, 8, 8, 14, 1, 5, 0, 6, 5, 8, 10, 15, 9, 14, 16,
             11, 1, 13]  # 29
    print(Solution().longestWPI(hours))
    print(Solution().longestWPI_square(hours))


if __name__ == "__main__":
    main()
