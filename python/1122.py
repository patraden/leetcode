from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        h = set(arr2)
        counter = Counter()
        suffix = []

        for num in arr1:
            if num in h:
                counter[num] += 1
            else:
                suffix.append(num)

        res = []
        for num in arr2:
            res += [num] * counter[num]
        res += sorted(suffix)
        return res


def test():
    print(Solution().relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
    print(Solution().relativeSortArray(arr1=[28, 6, 22, 8, 44, 17], arr2=[22, 28, 8, 6]))


if __name__ == '__main__':
    test()
