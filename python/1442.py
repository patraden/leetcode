from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        d = {0: [-1]}
        res = prefix = 0
        for j, num in enumerate(arr):
            prefix ^= num
            for i in d.setdefault(prefix, []):
                res += j - i - 1
            d[prefix].append(j)
        return res


def test():
    print(Solution().countTriplets(arr=[2, 3, 1, 6, 7]))
    print(Solution().countTriplets(arr=[1, 1, 1, 1, 1]))


if __name__ == '__main__':
    test()
