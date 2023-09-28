from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = [-1] * n
        right = [n] * n

        stack = []
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            m = right[i] - left[i] - 1
            if nums[i] > threshold / m:
                return m

        return -1


def main():
    print(Solution().validSubarraySize(nums=[1, 3, 4, 3, 1], threshold=6))
    # print(Solution().validSubarraySize(nums=[6, 5, 6, 5, 8], threshold=7))
    print(Solution().validSubarraySize(nums=[1, 1, 1, 1, 1, 1, 1], threshold=6))
    # print(Solution().validSubarraySize(nums=[1, 7], threshold=2))


if __name__ == "__main__":
    main()
