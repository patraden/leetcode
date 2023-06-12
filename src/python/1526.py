from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and target[stack[-1]] > target[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        res = 0
        stack = [(0, n)]
        for i in range(n):
            base, idx = stack[-1]
            if idx == i:
                stack.pop()
                stack.append((target[i], right[i]))
                continue

            if target[i] > base:
                res += target[i] - base
                stack.append((target[i], right[i]))

        return res


def main():
    print(Solution().minNumberOperations([1, 2, 3, 2, 1]))
    print(Solution().minNumberOperations([3, 1, 1, 2]))
    print(Solution().minNumberOperations([3, 1, 5, 4, 2, 0, 4, 2, 2, 0]))


if __name__ == "__main__":
    main()
