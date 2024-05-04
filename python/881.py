from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l, r = 0, len(people) - 1

        res = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            res += 1
            r -= 1
        return res


def test():
    print(Solution().numRescueBoats(people=[1, 2], limit=3))
    print(Solution().numRescueBoats(people=[3, 2, 2, 1], limit=3))
    print(Solution().numRescueBoats(people=[3, 5, 3, 4], limit=5))
    print(Solution().numRescueBoats(people=[1], limit=5))


if __name__ == '__main__':
    test()
