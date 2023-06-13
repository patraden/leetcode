def largestRectangleArea(heights: list[int]):
    n = len(heights)
    left = [0] * n
    stack = [-1]
    for i in range(n):
        idx = stack[-1]
        while idx != -1 and heights[idx] >= heights[i]:
            stack.pop()
            idx = stack[-1]
        left[i] = idx
        stack.append(i)

    right = [0] * n
    stack = [n]
    for i in range(n - 1, -1, -1):
        idx = stack[-1]
        while idx != n and heights[idx] >= heights[i]:
            stack.pop()
            idx = stack[-1]
        right[i] = idx
        stack.append(i)

    res = 0
    for i in range(n):
        width = right[i] - left[i] - 1
        res = max(res, heights[i] * width)

    return res


def main():
    test1 = [2, 1, 5, 6, 2, 3]
    test2 = [1, 1]
    print(largestRectangleArea(test1))
    print(largestRectangleArea(test2))


if __name__ == "__main__":
    main()
