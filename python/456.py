from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        for k in nums:
            if not stack:
                stack.append((k, None))
            else:
                i, j = stack[-1]
                if k < i:
                    stack.append((k, None))
                elif k == i:
                    pass
                elif j is not None and k < j:
                    return True
                else:
                    i, j = i, k
                    while stack and (i <= stack[-1][0]) and (stack[-1][1] is None or j >= stack[-1][1]):
                        stack.pop()
                    if stack and stack[-1][0] < k:
                        return True
                    stack.append((i, j))
        return False


def main():
    print(Solution().find132pattern(nums=[3, 5, 0, 3, 4]))
    print(Solution().find132pattern(nums=[3, 1, 4, 2]))
    print(Solution().find132pattern(nums=[1, 2, 3, 4]))
    print(Solution().find132pattern(nums=[-1, 3, 2, 0]))


if __name__ == "__main__":
    main()
