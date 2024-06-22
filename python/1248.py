from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        p = [1]
        odds = res = 0
        for i, num in enumerate(nums):
            if num % 2 == 1:
                odds += 1
                p.append(0)

            p[odds] += 1
            if odds >= k:
                res += p[odds - k]

        return res


def test():
    print(Solution().numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
    print(Solution().numberOfSubarrays(nums=[2, 4, 6], k=1))
    print(Solution().numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))


if __name__ == '__main__':
    test()
