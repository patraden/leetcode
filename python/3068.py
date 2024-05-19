from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        flips = s = 0
        diff = float('inf')
        for num in nums:
            if (num ^ k) > num:
                flips += 1
                s += (num ^ k)
            else:
                s += num
            diff = min(diff, abs((num ^ k) - num))

        if flips % 2 == 0:
            return s
        return s - diff




def test():
    print(Solution().maximumValueSum(nums=[1, 2, 1], k=3, edges=[[0, 1], [0, 2]]))
    print(Solution().maximumValueSum(nums=[2, 3], k=7, edges=[[0, 1]]))
    print(Solution().maximumValueSum(nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]))
    print(Solution().maximumValueSum(
        nums=[24, 78, 1, 97, 44],
        k=6,
        edges=[[0, 2], [1, 2], [4, 2], [3, 4]])
    )


if __name__ == '__main__':
    test()
