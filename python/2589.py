from typing import List


class Solution:
    @staticmethod
    def binsearch(stack: List[List], start: int, end: int, duration: int) -> List[List]:
        #  find runtime prefix to exclude (runtime before start)
        l, r = 0, len(stack)
        while l < r:
            m = (l + r) // 2
            if start > stack[m][1]:
                l = m + 1
            else:
                r = m

        if r == len(stack):
            stack.append([end - duration + 1, end, duration + (stack[-1][2] if stack else 0)])
            return stack

        skipped = max(start, stack[r][0]) - stack[r][0] + (stack[r - 1][2] if r > 0 else 0)
        available = stack[-1][2] - skipped
        remainder = duration - available

        # everything can be overlapped with previous tasks
        if remainder <= 0:
            return stack

        # task is longer than all previous task
        if end - duration + 1 <= stack[0][0]:
            return [[end - duration + 1, end, duration]]

        while stack[-1][1] >= (end - remainder + 1):
            s, e, _ = stack.pop()
            available -= e - s + 1
            remainder += e - s + 1

        stack.append([end - remainder + 1, end, available + skipped + remainder])
        return stack

    def findMinimumTime(self, tasks: List[List[int]]) -> int:

        runtime = 0  # current total accumulative runtime
        stack = []  # (start, end, current total accumulative runtime)
        for start, end, duration in sorted(tasks, key=lambda a: a[1]):
            stack = self.binsearch(stack, start, end, duration)

        return stack[-1][2]


def main():
    s = Solution()
    # print(s.binsearch(stack=[[5, 8, 4], [10, 12, 7], [15, 21, 14]], start=0, end=23, duration=24))
    print(s.findMinimumTime(tasks=[[10, 18, 2], [1, 8, 1], [10, 20, 8]]))
    print(s.findMinimumTime(tasks=[[2, 3, 1], [4, 5, 1], [1, 5, 2]]))
    print(s.findMinimumTime(tasks=[[1, 3, 2], [2, 5, 3], [5, 6, 2]]))


if __name__ == "__main__":
    main()
