from typing import List
import heapq


class Solution:
    def avoidFlood(self, rains: List[int]) -> list[int]:

        rained = set()
        next_rained = []
        ans = [-1] * len(rains)

        met = {}
        for i in range(len(rains) - 1, -1, -1):
            if rains[i] != 0:
                if rains[i] in met:
                    ans[i] = met[rains[i]]
                met[rains[i]] = i

        for i, rain in enumerate(rains):
            if rain in rained:
                return []

            if rain == 0:
                if next_rained:
                    _, next_rain = heapq.heappop(next_rained)
                    ans[i] = next_rain
                    rained.remove(next_rain)
                else:
                    ans[i] = 1
                continue

            if ans[i] != -1:  # element is worth adding
                rained.add(rain)
                heapq.heappush(next_rained, (ans[i], rain))
            ans[i] = -1

        return ans


def test():
    assert Solution().avoidFlood(rains=[1, 2, 3, 4]) == [-1, -1, -1, -1]
    assert Solution().avoidFlood(rains=[1, 22, 0, 0, 22, 1]) == [-1, -1, 22, 1, -1, -1]
    assert Solution().avoidFlood(rains=[1, 2, 0, 1, 2]) == []
    assert Solution().avoidFlood(rains=[33, 2, 152, 44, 0, 0, 44, 152, 0]) == [-1, -1, -1, -1, 44, 152, -1, -1, 1]
    assert Solution().avoidFlood(rains=[0, 1, 1]) == []
    assert Solution().avoidFlood(rains=[11, 0, 2, 0, 11, 2, 33, 0, 33]) == [-1, 11, -1, 2, -1, -1, -1, 33, -1]
    assert Solution().avoidFlood(rains=[11, 0, 2, 0, 11, 2, 33, 0, 33, 2]) == []
    assert Solution().avoidFlood(rains=[69, 0, 0, 0, 69]) == [-1, 69, 1, 1, -1]
    assert Solution().avoidFlood(rains=[1, 2, 0, 2, 3, 0, 1]) == [-1, -1, 2, -1, -1, 1, -1]
    rains = [0, 72328, 0, 0, 94598, 54189, 39171, 53361, 0, 0, 0, 72742, 0, 98613, 16696, 0, 32756, 23537, 0, 94598, 0,
             0, 0, 11594, 27703, 0, 0, 0, 20081, 0, 24645, 0, 0, 0, 0, 0, 0, 0, 2711, 98613, 0, 0, 0, 0, 0, 91987, 0, 0,
             0, 22762, 23537, 0, 0, 0, 0, 54189, 0, 0, 87770, 0, 0, 0, 0, 27703, 0, 0, 0, 0, 20081, 16696, 0, 0, 0, 0,
             0, 0, 0, 35903, 0, 72742, 0, 0, 0, 35903, 0, 0, 91987, 76728, 0, 0, 0, 0, 2711, 0, 0, 11594, 0, 0, 22762,
             24645, 0, 0, 0, 0, 0, 53361, 0, 87770, 0, 0, 39171, 0, 24577, 0, 0, 0, 24577, 0, 0, 72328, 0, 0, 32756, 0,
             0, 76728]
    expected = [1, -1, 72328, 1, -1, -1, -1, -1, 94598, 54189, 53361, -1, 72742, -1, -1, 98613, -1, -1, 23537, -1,
                16696, 39171, 32756, -1, -1, 27703, 11594, 1, -1, 20081, -1, 24645, 1, 1, 1, 1, 1, 1, -1, -1, 2711, 1,
                1, 1, 1, -1, 91987, 1, 1, -1, -1, 22762, 1, 1, 1, -1, 1, 1, -1, 87770, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1,
                1, 1, 1, 1, 1, 1, 1, -1, 35903, -1, 1, 1, 1, -1, 1, 1, -1, -1, 76728, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1,
                -1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 24577, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1]

    assert Solution().avoidFlood(rains) == expected


if __name__ == '__main__':
    test()
