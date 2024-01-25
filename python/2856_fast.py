from typing import List


class Solution:
    """
    We store the count of the element that occurs maximum number of times.
    Notice that if the count of max occuring element is less than n/2 times,
    then the element can be cancelled by remaining elements
    (It is given that elements are sorted in non-decreasing order.
    Hence, all remaining elements will be cancelled amongst themselves).
    In this case, if array size is even, then we say that ans is 0 and 1 incase the array size is odd.
    Because after cancelling all elements, 1 element is still remaining at the end.
    If the element occurs more than n/2 times, so now it cannot cancel all elements.
    But it will still cancel all remaining elements.
    How many elements are remaining? The elements remaining are (n - maxi). So elements left are maxi - (n - maxi) = 2*maxi - n;
    """
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.setdefault(num, 0) + 1

        _max = 1
        for f in d:
            _max = max(_max, d[f])

        if _max <= len(nums) // 2:
            return len(nums) % 2
        return 2*_max - len(nums)



def test():
    print(Solution().minLengthAfterRemovals(nums=[1, 1, 2]))
    print(Solution().minLengthAfterRemovals(nums=[1, 1, 2, 2, 2, 3, 3, 3, 3, 3]))
    print(Solution().minLengthAfterRemovals(nums=[1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4]))
    print(Solution().minLengthAfterRemovals(nums=[2, 3, 6, 9]))
    print(Solution().minLengthAfterRemovals(nums=[1, 2, 2, 2, 3, 3]))


if __name__ == '__main__':
    test()
