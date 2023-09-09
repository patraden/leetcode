from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        prefixes = set()
        _max = _assumed_max = mask = 0

        for b in range(31, -1, -1):
            mask |= 1 << b
            _assumed_max = _max | (1 << b)
            for num in nums:
                prefixes.add(mask & num)

            for prefix in prefixes:
                if (_assumed_max ^ prefix) in prefixes:
                    _max = _assumed_max
                    break
            prefixes.clear()

        return _max
