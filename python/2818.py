from typing import List
from functools import cache


class Solution:
    mod = 1_000_000_007

    @cache
    def prime_score(self, num: int):
        if num == 0:
            return float('inf')
        if num == 1:
            return 0
        i = 2
        while i * i <= num:
            if num % i == 0:
                if (num // i) % i == 0:
                    return self.prime_score(num // i)
                return 1 + self.prime_score(num // i)
            i += 1
        return 1

    def pow(self, num, p):
        res = 1
        while p > 0:
            if p % 2 == 1:
                res = (res * num) % self.mod
            num = (num * num) % self.mod
            p //= 2
        return res

    def maximumScore(self, nums: List[int], k: int) -> int:
        nums.append(0)
        sub_arrays = [None] * (len(nums) - 1)  # contains count of sub arrays where i-th element has max prime_score
        stack = []
        for current in range(len(nums)):
            while stack and self.prime_score(nums[current]) > self.prime_score(nums[stack[-1][0]]):
                prev, before = stack.pop()
                sub_arrays[prev] = (nums[prev], before * (current - prev))
            before = current - (stack[-1][0] if stack else -1)
            stack.append((current, before))

        i, res = 0, 1
        for num, m in sorted(sub_arrays, reverse=True):
            if (i + m) >= k:
                res *= self.pow(num, (k - i)) % self.mod
                return res % self.mod
            res *= self.pow(num, m) % self.mod
            i += m


def main():
    print(Solution().maximumScore([1, 7, 11, 1, 5], k=14))  # expected 823751938 561 / 869 test cases passed.
    print(Solution().maximumScore([8, 3, 9, 3, 8], k=2))
    print(Solution().maximumScore([19, 12, 14, 6, 10, 18], k=3))


if __name__ == "__main__":
    main()
