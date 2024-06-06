from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter = Counter(hand)
        for card in hand:
            start = card
            while counter[start - 1]:
                start -= 1

            while counter[start]:
                for i in range(groupSize):
                    if not counter[start + i]:
                        return False
                    counter[start + i] -= 1
        return True


def test():
    print(Solution().isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))
    print(Solution().isNStraightHand(hand=[1, 2, 1, 1, 2, 3, 2, 3, 3], groupSize=3))
    print(Solution().isNStraightHand(hand=[1, 2, 3, 4, 5, 6], groupSize=2))
    print(Solution().isNStraightHand(hand=[2, 1], groupSize=2))


if __name__ == '__main__':
    test()
