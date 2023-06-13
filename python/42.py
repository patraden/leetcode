def trap(height: list[int]):
    n = len(height)
    left = [0] * n
    stack = [-1]
    for i in range(0, n):
        idx = stack[-1]
        while idx != -1 and height[idx] <= height[i]:
            stack.pop()
            idx = stack[-1]
        left[i] = idx
        stack.append(i)

    right = [0] * n
    stack = [n]
    for i in range(n - 1, -1, -1):
        idx = stack[-1]
        while idx != n and height[idx] <= height[i]:
            stack.pop()
            idx = stack[-1]
        right[i] = idx
        stack.append(i)

    res = 0
    for h, l, r in set([(height[i], left[i], right[i]) for i in range(n) if (left[i] != -1 and right[i] != n)]):
        border = min(height[l], height[r])
        res += (border - h) * (r - l - 1)
    return res


def main():
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height2 = [4, 2, 0, 3, 2, 5]
    print(trap(height1))
    print(trap(height2))


if __name__ == "__main__":
    main()
