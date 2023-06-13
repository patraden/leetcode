def firstMissingPositive(nums: list[int]) -> int:
    _min_positive = None
    nums.append(-1)
    n = len(nums)
    for i in range(n):
        if 0 < nums[i] < n:
            if not _min_positive or nums[i] < _min_positive:
                _min_positive = nums[i]
        else:
            nums[i] = None

    #  _min_positive is None == "all negative"
    #  _min_positive > 1 == "1 is free"
    if _min_positive is None or _min_positive != 1:
        return 1

    for i in range(n):
        if nums[i] is not None:
            k = nums[i]
            while (k and k != i) and (nums[k] is None or nums[k] != k):
                nums[i], nums[k] = nums[k], nums[i]
                k = nums[i]
            if nums[i] and nums[i] != i:
                nums[i] = None
    for i in range(1, n):
        if not nums[i]:
            return i
    return n


def main():
    print(firstMissingPositive([3, 1]))
    print(firstMissingPositive([1, 2, 0]))
    print(firstMissingPositive([3, 4, -1, 1]))
    print(firstMissingPositive([7, 8, 9, 11, 12]))
    print(firstMissingPositive([1, 2, 2, 2, 4, 2]))
    print(firstMissingPositive([0, 3, 2, 1, 4, 7, 5, 6]))
    print(firstMissingPositive([-1, 7, -2, 0, 11, 5, 10, 6, 3, 4, 1, 2]))


if __name__ == "__main__":
    main()
