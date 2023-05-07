#  https://leetcode.com/problems/maximum-subarray/

def max_sub_array(nums: list[int]) -> int:
    _max = prev = nums[0]
    for i in range(1, len(nums)):
        current = nums[i] if prev + nums[i] < nums[i] else prev + nums[i]
        _max = max(current, _max)
        prev = current
    return _max


def main():
    test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    test2 = [1]
    test3 = [5, 4, -1, 7, 8]
    assert max_sub_array(test1) == 6
    assert max_sub_array(test2) == 1
    assert max_sub_array(test3) == 23


if __name__ == "__main__":
    main()
