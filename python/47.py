def permute(nums: list) -> list:
    res = {}
    n = len(nums)

    def permute_helper(prefix_idx=None, prefix_nums=None, prefix_str=None):

        prefix_idx = prefix_idx or []
        prefix_nums = prefix_nums or []
        prefix_str = prefix_str or ""
        if len(prefix_idx) == len(nums):
            if prefix_str not in res:
                res[prefix_str] = prefix_nums

        for i in range(n):
            if i in prefix_idx:
                continue
            prefix_idx.append(i)
            prefix_nums.append(nums[i])
            permute_helper(
                prefix_idx.copy(),
                prefix_nums.copy(),
                prefix_str + "," + str(nums[i]) if prefix_str else str(nums[i])
            )
            prefix_idx.pop()
            prefix_nums.pop()

    permute_helper()
    return list(res.values())


def main():
    test1 = [1]
    test2 = [12, 12]
    test3 = [1, 1, 2]
    test4 = [1, 2, 2, 2]
    test5 = [1, 2, 3, 4, 5]
    test6 = [1, 2, 2, 4, 5, 6]
    # print(permute(test1))
    # print(permute(test2))
    # print(permute(test3))
    print(permute(test4))
    # print(permute(test5))
    # print(permute(test6))


if __name__ == "__main__":
    main()
