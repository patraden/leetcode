def algo():
    nums = [2, 3, 2, 5, 2, 7]
    k = 3
    h = set()
    for i in range(len(nums)):
        if nums[i] in h:
            return True
        h.add(nums[i])
        if i - k >= 0:
            h.remove(nums[i - k])
    return False


if __name__ == "__main__":
    print(algo())
