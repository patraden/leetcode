def removeDuplicates(nums: list[int]) -> int:
    n = len(nums)
    j = 0
    last = nums[j]
    for i in range(1, n):
        if nums[i] > last:
            last = nums[i]
            j += 1
            nums[j] = last
        if i == n - 1:
            for k in range(j + 1, n):
                nums[k] = None
    return j + 1

def main():
    print(removeDuplicates([1, 1, 1, 2, 2, 2, 2, 3, 3]))
    print(removeDuplicates([1, 2, 3, 4, 4, 66, 66, 66]))
    print(removeDuplicates([2, 2, 2, 2]))


if __name__ == "__main__":
    main()
