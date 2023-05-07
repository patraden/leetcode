#  https://leetcode.com/problems/sliding-window-maximum/

from collections import deque


def main():
    with open("input.txt", "r") as f:
        k = int(f.readline().rstrip())
        nums = list(map(int, f.readline().rstrip().split()))
        n = len(nums)

    q = deque()
    res = []
    for i in range(n):
        if i > k - 1:
            res.append(nums[q[0]])
            while q and q[0] <= i - k:
                q.popleft()
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
    res.append(nums[q[0]])

    print(*res)


if __name__ == "__main__":
    main()
