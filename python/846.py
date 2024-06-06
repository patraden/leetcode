from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter = Counter(hand)
        for card in sorted(counter.keys()):
            while counter[card]:
                for i in range(groupSize):
                    if counter[card + i] == 0:
                        return False
                    counter[card + i] -= 1

        return True


def test():
    print(Solution().isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))
    print(Solution().isNStraightHand(hand=[1, 2, 1, 1, 2, 3, 2, 3, 3], groupSize=3))


if __name__ == '__main__':
    test()
