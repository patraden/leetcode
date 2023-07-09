from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 1_000_000_007
        n = len(arr)
        left = [0] * n
        right = [0] * n

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        res = 0
        for i in range(n):
            res += (
                    (i - left[i]) * arr[i] +
                    (right[i] - i - 1) * arr[i] +
                    (i - left[i] - 1) * (right[i] - i - 1) * arr[i]
                    ) % mod

        return res % mod


def main():
    print(Solution().sumSubarrayMins([3, 1, 2, 4]))
    print(Solution().sumSubarrayMins([1, 1, 1, 1, 1]))
    print(Solution().sumSubarrayMins([11, 81, 94, 43, 3]))


if __name__ == "__main__":
    main()
