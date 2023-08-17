from typing import List
from functools import cache


class Solution:
    @cache
    def gcd(self, a: int, b: int) -> int:
        if a < b:  # a >= b
            a, b = b, a
        return b if a % b == 0 else self.gcd(b, a % b)

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = [nums[0]]
        for num in nums[1:]:
            curr = num
            while stack and self.gcd(curr, stack[-1]) > 1:
                prev = stack.pop()
                curr = curr * prev // self.gcd(curr, prev)
            stack.append(curr)
        return stack


def main():
    print(Solution().replaceNonCoprimes([6, 4, 3, 2, 7, 6, 2]))
    print(Solution().replaceNonCoprimes([2, 2, 1, 1, 3, 3, 3]))
    print(Solution().replaceNonCoprimes([2]))


if __name__ == "__main__":
    main()
