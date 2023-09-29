from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(-1)
        # when new item pops old num
        # it means that item it popped is no longer minimum for relevant subarray
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                k = stack.pop()
                s = -1 if not stack else stack[-1]
                m = i - s - 1
                if nums[k] > threshold / m:
                    return m
            stack.append(i)
        return -1


def main():
    print(Solution().validSubarraySize(nums=[1, 3, 4, 3, 1], threshold=6))
    print(Solution().validSubarraySize(nums=[6, 5, 6, 5, 8], threshold=7))
    print(Solution().validSubarraySize(nums=[1, 1, 1, 1, 1, 1, 1], threshold=6))


if __name__ == "__main__":
    main()
