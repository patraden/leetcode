def permute(nums: list) -> list:
    res = []

    def permute_helper(prefix=None):

        prefix = prefix or []
        if len(prefix) == len(nums):
            res.append(prefix)

        for num in nums:
            if num in prefix:
                continue
            prefix.append(num)
            permute_helper(prefix.copy())
            prefix.pop()

    permute_helper()
    return res


def main():
    test1 = [1]
    test2 = [12, 3]
    test3 = [1, 2, 3]
    test4 = [1, 2, 3, 4]
    test5 = [1, 2, 3, 4, 5]
    test6 = [1, 2, 3, 4, 5, 6]
    print(permute(test1))
    print(permute(test2))
    print(permute(test3))
    print(permute(test4))
    print(permute(test5))
    print(permute(test6))


if __name__ == "__main__":
    main()
