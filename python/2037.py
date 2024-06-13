from typing import List
from functools import reduce


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return reduce(lambda x, y: x + y, map(lambda t: abs(t[0] - t[1]), zip(sorted(seats), sorted(students))))


def test():
    print(Solution().minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]))
    print(Solution().minMovesToSeat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]))
    print(Solution().minMovesToSeat(seats=[2, 2, 6, 6], students=[1, 3, 2, 6]))


if __name__ == '__main__':
    test()
