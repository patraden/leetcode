from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        right = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            qty = 0
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
                qty += 1
            right[i] = qty + 1 if stack else qty
            stack.append(i)

        return right


def main():
    print(Solution().canSeePersonsCount([10, 6, 8, 5, 11, 9]))
    print(Solution().canSeePersonsCount([5, 1, 2, 3, 10]))
    print(Solution().canSeePersonsCount([9, 10]))


if __name__ == "__main__":
    main()
